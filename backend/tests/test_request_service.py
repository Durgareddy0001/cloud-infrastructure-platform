import os
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

os.environ.setdefault("APP_NAME", "Cloud Platform Test")
os.environ.setdefault("APP_VERSION", "test")
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("HOST", "127.0.0.1")
os.environ.setdefault("PORT", "8000")
os.environ.setdefault("DATABASE_URL", "sqlite://")

from app.core.database import Base
from app.models.infrastructure_request import InfrastructureRequest as InfrastructureRequestModel
from app.schemas.request import InfrastructureRequest, RequestStatus
from app.services.request_service import (
    create_infrastructure_request,
    delete_infrastructure_request,
    get_all_infrastructure_requests,
    get_infrastructure_request,
    update_infrastructure_request_status,
)


class InfrastructureRequestServiceTests(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()
        self.request = InfrastructureRequest(
            application_name="payments",
            environment="dev",
            region="asia-south1",
            namespace="payments-dev",
            cpu="2",
            memory="4Gi",
            node_pool="default-pool",
        )

    def tearDown(self):
        self.session.close()

    def test_create_and_get_request(self):
        created = create_infrastructure_request(self.request, self.session)

        fetched = get_infrastructure_request(created.request_id, self.session)

        self.assertEqual(fetched.application_name, "payments")
        self.assertEqual(fetched.status, RequestStatus.PENDING.value)

    def test_list_and_update_status(self):
        created = create_infrastructure_request(self.request, self.session)

        updated = update_infrastructure_request_status(
            created.request_id,
            RequestStatus.IN_PROGRESS,
            self.session,
        )

        self.assertEqual(updated.status, RequestStatus.IN_PROGRESS.value)
        self.assertEqual(len(get_all_infrastructure_requests(self.session)), 1)

    def test_delete_request(self):
        created = create_infrastructure_request(self.request, self.session)

        delete_infrastructure_request(created.request_id, self.session)

        self.assertEqual(
            self.session.query(InfrastructureRequestModel).count(),
            0,
        )

    def test_unknown_request_returns_not_found(self):
        with self.assertRaisesRegex(Exception, "Infrastructure request not found"):
            get_infrastructure_request("missing", self.session)


if __name__ == "__main__":
    unittest.main()
