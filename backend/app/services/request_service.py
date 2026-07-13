from uuid import uuid4

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.infrastructure_request_repository import (
    InfrastructureRequestRepository,
)
from app.schemas.request import (
    InfrastructureRequest,
    RequestStatus,
)
from app.schemas.response import InfrastructureResponse, InfrastructureRequestResponse


def create_infrastructure_request(
    request: InfrastructureRequest,
    db: Session,
) -> InfrastructureResponse:

    repository = InfrastructureRequestRepository(db)

    request_id = str(uuid4())

    saved_request = repository.create_request(
        request=request,
        request_id=request_id,
    )

    return InfrastructureResponse(
        request_id=saved_request.request_id,
        application_name=saved_request.application_name,
        status=saved_request.status,
        message="Infrastructure request created successfully.",
    )


def get_all_infrastructure_requests(db: Session):
    repository = InfrastructureRequestRepository(db)
    return repository.get_all_requests()


def get_infrastructure_request(
    request_id: str,
    db: Session,
) -> InfrastructureRequestResponse:
    repository = InfrastructureRequestRepository(db)
    saved_request = repository.get_request_by_id(request_id)
    if saved_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Infrastructure request not found.",
        )
    return saved_request


def update_infrastructure_request_status(
    request_id: str,
    request_status: RequestStatus,
    db: Session,
) -> InfrastructureRequestResponse:
    repository = InfrastructureRequestRepository(db)
    saved_request = repository.get_request_by_id(request_id)
    if saved_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Infrastructure request not found.",
        )
    return repository.update_status(saved_request, request_status)


def delete_infrastructure_request(request_id: str, db: Session) -> None:
    repository = InfrastructureRequestRepository(db)
    saved_request = repository.get_request_by_id(request_id)
    if saved_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Infrastructure request not found.",
        )
    repository.delete_request(saved_request)
