from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.mongo_uri)
# Use a sensible default database name when none is provided in the URI.
DEFAULT_DB = "internpilot"
try:
	db = client.get_default_database()
except Exception:
	db = client.get_database(DEFAULT_DB)

users_collection = db.get_collection("users")
applications_collection = db.get_collection("applications")
companies_collection = db.get_collection("companies")
notifications_collection = db.get_collection("notifications")
interviews_collection = db.get_collection("interviews")
