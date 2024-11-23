from django.db import OperationalError
from django.test import Client
from infrastructure.service_locator.mock_services import MockTimeService
from infrastructure.tests.view_fixtures import view_test
from main_app.accounts.tests.api_fixtures import *
from main_app.health.tests.api_fixtures import *
from typing import Any

@view_test
def test_get_health_status(
    anonymous_client: Client,
    get_health_status: StatusType,
    mock_time_service: MockTimeService,
) -> None:
    response = get_health_status(anonymous_client)
    assert response.status == "ok"
    assert response.time == mock_time_service.current_time.isoformat()


@view_test
def test_get_health_status_error(
    anonymous_client: Client,
    get_health_status: StatusType,
    mocker: Any,
    mock_time_service: MockTimeService,
) -> None:
    mocker.patch(
        "django.db.connection.ensure_connection",
        side_effect=OperationalError("Simulated connection failure"),
    )
    response = get_health_status(anonymous_client)
    assert response.status == "error"
    assert response.time == mock_time_service.current_time.isoformat()
