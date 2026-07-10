from pydantic import BaseModel
from typing import Optional


class InfrastructureRequest(BaseModel):

    application_name: str

    environment: str

    region: str

    namespace: str

    cpu: Optional[str] = None

    memory: Optional[str] = None

    node_pool: Optional[str] = None

    storage_bucket: Optional[str] = None

    bigquery_dataset: Optional[str] = None

    service_account: Optional[str] = None