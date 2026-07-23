from bson.objectid import ObjectId
from fastapi import HTTPException, status
from app.db.client import companies_collection
from app.schemas.company import CompanyCreate, CompanyUpdate


def create_company(user_id: str, payload: CompanyCreate) -> dict:
    data = payload.model_dump()
    data["user_id"] = user_id
    data["created_at"] = __import__("datetime").datetime.utcnow()
    result = companies_collection.insert_one(data)
    data["id"] = str(result.inserted_id)
    return data


def get_companies(user_id: str) -> list[dict]:
    cursor = companies_collection.find({"user_id": user_id}).sort("created_at", -1)
    return [{**item, "id": str(item["_id"])} for item in cursor]


def get_company(user_id: str, company_id: str) -> dict:
    company = companies_collection.find_one({"_id": ObjectId(company_id), "user_id": user_id})
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    company["id"] = str(company["_id"])
    return company


def update_company(user_id: str, company_id: str, payload: CompanyUpdate) -> dict:
    update_data = payload.model_dump(exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data to update")
    companies_collection.update_one({"_id": ObjectId(company_id), "user_id": user_id}, {"$set": update_data})
    return get_company(user_id, company_id)


def delete_company(user_id: str, company_id: str):
    result = companies_collection.delete_one({"_id": ObjectId(company_id), "user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return {"message": "Company deleted successfully"}
