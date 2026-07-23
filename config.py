import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_URI")
        self.jwt_secret = os.getenv("JWT_SECRET")
        self.jwt_algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        self.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
        self.email_from = os.getenv("EMAIL_FROM")
        self.admin_email = os.getenv("ADMIN_EMAIL")


settings = Settings()
