from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user
from app.services.user_service import get_user_by_id, update_profile
from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: dict = Depends(get_current_user)):
    return get_user_by_id(str(current_user["_id"]))

@router.patch("/me", response_model=UserResponse)
def update_current_user(payload: dict, current_user: dict = Depends(get_current_user)):
    return update_profile(str(current_user["_id"]), payload)
