from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class RequestStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class InfrastructureRequest(BaseModel):

    application_name: str = Field(min_length=1, max_length=100)

    environment: str = Field(min_length=1, max_length=20)

    region: str = Field(min_length=1, max_length=50)

    namespace: str = Field(min_length=1, max_length=100)

    cpu: str = Field(min_length=1, max_length=20)

    memory: str = Field(min_length=1, max_length=20)

    node_pool: str = Field(min_length=1, max_length=100)

    storage_bucket: Optional[str] = None

    bigquery_dataset: Optional[str] = None

    service_account: Optional[str] = None


class InfrastructureRequestStatusUpdate(BaseModel):
    status: RequestStatus
