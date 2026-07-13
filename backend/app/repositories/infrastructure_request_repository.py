from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Pydantic schema (used only for input)
from app.schemas.request import InfrastructureRequest, RequestStatus

# SQLAlchemy model (used for database)
from app.models.infrastructure_request import InfrastructureRequest as InfrastructureRequestModel


class InfrastructureRequestRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_request(
        self,
        request: InfrastructureRequest,
        request_id: str,
    ) -> InfrastructureRequestModel:

        db_request = InfrastructureRequestModel(
            request_id=request_id,
            application_name=request.application_name,
            environment=request.environment,
            namespace=request.namespace,
            region=request.region,
            cpu=request.cpu,
            memory=request.memory,
            node_pool=request.node_pool,
            storage_bucket=request.storage_bucket,
            bigquery_dataset=request.bigquery_dataset,
            service_account=request.service_account,
            status="PENDING",
        )

        self.db.add(db_request)
        self._commit()
        self.db.refresh(db_request)

        return db_request

    def get_all_requests(self):
        return self.db.query(InfrastructureRequestModel).all()

    def get_request_by_id(self, request_id: str):
        return (
            self.db.query(InfrastructureRequestModel)
            .filter(InfrastructureRequestModel.request_id == request_id)
            .first()
        )

    def update_status(
        self,
        request: InfrastructureRequestModel,
        status: RequestStatus,
    ) -> InfrastructureRequestModel:
        request.status = status.value
        self._commit()
        self.db.refresh(request)
        return request

    def delete_request(self, request: InfrastructureRequestModel) -> None:
        self.db.delete(request)
        self._commit()

    def _commit(self) -> None:
        try:
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise
