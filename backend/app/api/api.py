from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.requests import router as request_router


api_router = APIRouter()


api_router.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)


api_router.include_router(
    request_router,
    prefix="/api/v1",
    tags=["Infrastructure Requests"]
)

