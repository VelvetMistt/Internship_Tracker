from bson.objectid import ObjectId
from fastapi import HTTPException, status
from app.db.client import users_collection


def get_user_by_id(user_id: str) -> dict:
    user = users_collection.find_one({"_id": ObjectId(user_id)}, {"password": 0})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user["id"] = str(user["_id"])
    return user


def update_profile(user_id: str, payload: dict) -> dict:
    allowed_fields = {"name", "email"}
    update_data = {k: v for k, v in payload.items() if k in allowed_fields}
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No valid fields to update")

    users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return get_user_by_id(user_id)
