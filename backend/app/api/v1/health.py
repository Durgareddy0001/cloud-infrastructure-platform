from fastapi import APIRouter
from app.core.settings import settings

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment
    }