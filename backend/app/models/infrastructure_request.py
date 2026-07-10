from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func

from app.core.database import Base


class InfrastructureRequest(Base):
    __tablename__ = "infrastructure_requests"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Business Request ID
    request_id = Column(String(50), unique=True, nullable=False, index=True)

    # Request Details
    application_name = Column(String(100), nullable=False)
    environment = Column(String(20), nullable=False)
    namespace = Column(String(100), nullable=False)
    region = Column(String(50), nullable=False)

    # Infrastructure Configuration
    cpu = Column(String(20), nullable=False)
    memory = Column(String(20), nullable=False)
    node_pool = Column(String(100), nullable=False)

    storage_bucket = Column(String(100), nullable=True)
    bigquery_dataset = Column(String(100), nullable=True)
    service_account = Column(String(150), nullable=True)

    # Request Status
    status = Column(String(30), nullable=False, default="PENDING")

    # Audit Fields
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )