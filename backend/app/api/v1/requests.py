from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.request import InfrastructureRequest, InfrastructureRequestStatusUpdate
from app.schemas.response import InfrastructureRequestResponse, InfrastructureResponse
from app.services.request_service import (
    create_infrastructure_request,
    delete_infrastructure_request,
    get_all_infrastructure_requests,
    get_infrastructure_request,
    update_infrastructure_request_status,
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
    response_model=list[InfrastructureRequestResponse],
)
def get_requests(
    db: Session = Depends(get_db),
):
    return get_all_infrastructure_requests(db)


@router.get(
    "/requests/{request_id}",
    response_model=InfrastructureRequestResponse,
)
def get_request(request_id: str, db: Session = Depends(get_db)):
    return get_infrastructure_request(request_id, db)


@router.patch(
    "/requests/{request_id}/status",
    response_model=InfrastructureRequestResponse,
)
def update_request_status(
    request_id: str,
    request: InfrastructureRequestStatusUpdate,
    db: Session = Depends(get_db),
):
    return update_infrastructure_request_status(request_id, request.status, db)


@router.delete(
    "/requests/{request_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_request(request_id: str, db: Session = Depends(get_db)) -> Response:
    delete_infrastructure_request(request_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
