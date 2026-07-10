from uuid import uuid4
from sqlalchemy.orm import Session

from app.repositories.infrastructure_request_repository import (
    InfrastructureRequestRepository,
)
from app.schemas.request import InfrastructureRequest
from app.schemas.response import InfrastructureResponse


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