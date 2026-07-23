from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user
from app.services.company_service import create_company, get_companies, get_company, update_company, delete_company
from app.schemas.company import CompanyCreate, CompanyResponse, CompanyUpdate

router = APIRouter()

@router.post("/", response_model=CompanyResponse)
def create(payload: CompanyCreate, current_user: dict = Depends(get_current_user)):
    return create_company(str(current_user["_id"]), payload)

@router.get("/", response_model=list[CompanyResponse])
def list_companies(current_user: dict = Depends(get_current_user)):
    return get_companies(str(current_user["_id"]))

@router.get("/{company_id}", response_model=CompanyResponse)
def read_company(company_id: str, current_user: dict = Depends(get_current_user)):
    return get_company(str(current_user["_id"]), company_id)

@router.patch("/{company_id}", response_model=CompanyResponse)
def update(company_id: str, payload: CompanyUpdate, current_user: dict = Depends(get_current_user)):
    return update_company(str(current_user["_id"]), company_id, payload)

@router.delete("/{company_id}")
def delete(company_id: str, current_user: dict = Depends(get_current_user)):
    return delete_company(str(current_user["_id"]), company_id)
