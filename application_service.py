from bson.objectid import ObjectId
from fastapi import HTTPException, status
from app.db.client import applications_collection, companies_collection
from app.schemas.application import ApplicationCreate, ApplicationUpdate


def create_application(user_id: str, payload: ApplicationCreate) -> dict:
    company = companies_collection.find_one({"_id": ObjectId(payload.company_id)})
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")

    data = payload.model_dump()
    data["user_id"] = user_id
    data["created_at"] = __import__("datetime").datetime.utcnow()
    result = applications_collection.insert_one(data)
    data["id"] = str(result.inserted_id)
    return data


def get_applications(user_id: str) -> list[dict]:
    cursor = applications_collection.find({"user_id": user_id}).sort("created_at", -1)
    return [{**item, "id": str(item["_id"])} for item in cursor]


def get_application(user_id: str, application_id: str) -> dict:
    application = applications_collection.find_one({"_id": ObjectId(application_id), "user_id": user_id})
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    application["id"] = str(application["_id"])
    return application


def update_application(user_id: str, application_id: str, payload: ApplicationUpdate) -> dict:
    update_data = {k: v for k, v in payload.model_dump(exclude_none=True).items()}
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data to update")

    applications_collection.update_one(
        {"_id": ObjectId(application_id), "user_id": user_id},
        {"$set": update_data},
    )
    return get_application(user_id, application_id)


def delete_application(user_id: str, application_id: str):
    result = applications_collection.delete_one({"_id": ObjectId(application_id), "user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    return {"message": "Application deleted successfully"}
