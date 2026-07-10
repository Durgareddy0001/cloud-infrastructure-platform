from fastapi import FastAPI

from app.api.api import api_router
from app.core.database import Base, engine
from app.core.settings import settings

# Import models so SQLAlchemy knows about them
from app.models.infrastructure_request import InfrastructureRequest


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Cloud Infrastructure Self-Service Platform API"
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router)