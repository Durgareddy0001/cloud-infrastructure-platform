from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.request import InfrastructureRequest
from app.schemas.response import InfrastructureResponse
from app.services.request_service import (
    create_infrastructure_request,
    get_all_infrastructure_requests,
)

router = APIRouter()


@router.post(
    "/requests",
    response_model=InfrastructureResponse,
)
def create_request(
    request: InfrastructureRequest,
    db: Session = Depends(get_db),
):
    return create_infrastructure_request(request, db)


@router.get(
    "/requests",
    response_model=list[InfrastructureResponse],
)
def get_requests(
    db: Session = Depends(get_db),
):
    return get_all_infrastructure_requests(db)