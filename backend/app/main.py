import logging

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.api.api import api_router
from app.core.database import Base, engine
from app.core.settings import settings

# Import models so SQLAlchemy knows about them
from app.models.infrastructure_request import InfrastructureRequest


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Cloud Infrastructure Self-Service Platform API"
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.exception_handler(SQLAlchemyError)
async def database_exception_handler(
    request: Request,
    exc: SQLAlchemyError,
) -> JSONResponse:
    logger.exception("Database operation failed for %s", request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": "A database error occurred."},
    )
