from typing import Optional

from pydantic import BaseModel, ConfigDict


class InfrastructureResponse(BaseModel):
    request_id: str
    application_name: str
    status: str
    message: str

class InfrastructureRequestResponse(BaseModel):
    request_id: str
    application_name: str
    environment: str
    region: str
    namespace: str
    cpu: str
    memory: str
    node_pool: str
    storage_bucket: Optional[str] = None
    bigquery_dataset: Optional[str] = None
    service_account: Optional[str] = None
    status: str

    model_config = ConfigDict(from_attributes=True)
