import os

import pytest
from starlette.testclient import TestClient

from app.main import create_application
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=True, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    # set up
    application = create_application()
    application.dependency_overrides[get_settings] = get_settings_override

    with TestClient(application) as test_client:

        # testing
        yield test_client

    # tear down
