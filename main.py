from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.routes.auth import router as auth_router
from app.routes.users import router as user_router
from app.routes.applications import router as application_router
from app.routes.companies import router as company_router
from app.routes.dashboard import router as dashboard_router
from app.utils.exceptions import register_exception_handlers
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(
    title="InternPilot AI",
    description="Internship application lifecycle management platform for students.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_dir = os.path.join(os.path.dirname(__file__), "static")
assets_dir = os.path.join(static_dir, "assets")
app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

# Serve each HTML page explicitly so /login maps to login.html, not index.html.
def get_html_page(page_name: str):
    file_path = os.path.join(static_dir, f"{page_name}.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return FileResponse(os.path.join(static_dir, "index.html"))

@app.get("/")
def read_index():
    return get_html_page("index")

@app.get("/login")
def read_login():
    return get_html_page("login")

@app.get("/register")
def read_register():
    return get_html_page("register")

@app.get("/dashboard")
def read_dashboard():
    return get_html_page("dashboard")

@app.get("/applications")
def read_applications():
    return get_html_page("applications")

@app.get("/analytics")
def read_analytics():
    return get_html_page("analytics")

@app.get("/companies")
def read_companies():
    return get_html_page("companies")

@app.get("/calendar")
def read_calendar():
    return get_html_page("calendar")

@app.get("/profile")
def read_profile():
    return get_html_page("profile")

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(application_router, prefix="/api/applications", tags=["Applications"])
app.include_router(company_router, prefix="/api/companies", tags=["Companies"])
app.include_router(dashboard_router, prefix="/api/dashboard", tags=["Dashboard"])

register_exception_handlers(app)

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "InternPilot AI"}
