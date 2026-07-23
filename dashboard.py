from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user
from app.db.client import applications_collection, companies_collection

router = APIRouter()

@router.get("/summary")
def summary(current_user: dict = Depends(get_current_user)):
    user_id = str(current_user["_id"])
    applications = applications_collection.count_documents({"user_id": user_id})
    companies = companies_collection.count_documents({"user_id": user_id})
    status_breakdown = list(
        applications_collection.aggregate(
            [
                {"$match": {"user_id": user_id}},
                {"$group": {"_id": "$status", "count": {"$sum": 1}}},
            ]
        )
    )
    return {
        "applications": applications,
        "companies": companies,
        "status_breakdown": status_breakdown,
    }
