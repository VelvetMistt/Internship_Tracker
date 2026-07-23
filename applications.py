from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user
from app.services.application_service import create_application, get_applications, get_application, update_application, delete_application
from app.schemas.application import ApplicationCreate, ApplicationResponse, ApplicationUpdate

router = APIRouter()

@router.post("/", response_model=ApplicationResponse)
def create(payload: ApplicationCreate, current_user: dict = Depends(get_current_user)):
    return create_application(str(current_user["_id"]), payload)

@router.get("/", response_model=list[ApplicationResponse])
def list_applications(current_user: dict = Depends(get_current_user)):
    return get_applications(str(current_user["_id"]))

@router.get("/{application_id}", response_model=ApplicationResponse)
def read_application(application_id: str, current_user: dict = Depends(get_current_user)):
    return get_application(str(current_user["_id"]), application_id)

@router.patch("/{application_id}", response_model=ApplicationResponse)
def update(application_id: str, payload: ApplicationUpdate, current_user: dict = Depends(get_current_user)):
    return update_application(str(current_user["_id"]), application_id, payload)

@router.delete("/{application_id}")
def delete(application_id: str, current_user: dict = Depends(get_current_user)):
    return delete_application(str(current_user["_id"]), application_id)
