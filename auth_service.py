from datetime import timedelta
from fastapi import HTTPException, status
from app.db.client import users_collection
from app.utils.security import hash_password, verify_password, create_access_token, decode_access_token
from bson.objectid import ObjectId
from app.schemas.auth import SignupRequest, PasswordResetRequest, EmailVerificationRequest, PasswordResetConfirm


def register_user(payload: SignupRequest) -> dict:
    existing = users_collection.find_one({"email": payload.email})
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    hashed_password = hash_password(payload.password)
    user_data = {
        "name": payload.name,
        "email": payload.email,
        "password": hashed_password,
        "role": payload.role.value,
        "verified": False,
        "created_at": __import__("datetime").datetime.utcnow(),
    }
    result = users_collection.insert_one(user_data)
    user_data["_id"] = result.inserted_id
    return user_data


def authenticate_user(email: str, password: str) -> dict:
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    return user


def create_user_token(user_id: str) -> str:
    return create_access_token(subject=user_id, expires_delta=timedelta(minutes=60))


def generate_verification_token(user_id: str) -> str:
    return create_access_token(subject=user_id, expires_delta=timedelta(hours=24))


def request_password_reset(payload: PasswordResetRequest) -> dict:
    user = users_collection.find_one({"email": payload.email})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    reset_token = create_access_token(subject=str(user["_id"]), expires_delta=timedelta(minutes=30))
    return {
        "message": "Password reset requested. Use the token to reset your password.",
        "reset_token": reset_token,
    }


def verify_email(payload: EmailVerificationRequest) -> dict:
    try:
        token_data = decode_access_token(payload.token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid verification token")

    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token payload")

    users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"verified": True}})
    return {"message": "Email verified successfully."}


def reset_password(payload: PasswordResetConfirm) -> dict:
    try:
        token_data = decode_access_token(payload.token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid reset token")

    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token payload")

    users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"password": hash_password(payload.new_password)}})
    return {"message": "Password has been reset successfully."}
