from sqlalchemy.orm import Session

# Pydantic schema (used only for input)
from app.schemas.request import InfrastructureRequest

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
        self.db.commit()
        self.db.refresh(db_request)

        return db_request

    def get_all_requests(self):
        return self.db.query(InfrastructureRequestModel).all()