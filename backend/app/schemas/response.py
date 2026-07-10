from pydantic import BaseModel


class InfrastructureResponse(BaseModel):
    request_id: str
    application_name: str
    status: str
    message: str

    class Config:
        from_attributes = True


class InfrastructureRequestResponse(BaseModel):
    request_id: str
    application_name: str
    environment: str
    region: str
    namespace: str
    status: str

    class Config:
        from_attributes = True