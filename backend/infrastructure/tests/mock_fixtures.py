from typing import Generator

from infrastructure.service_locator.mock_services import MockTimeService
from infrastructure.service_locator.service_locator import (
    get_service_locator,
    set_service_locator,
)
from infrastructure.tests.mock_service_locator import MockServiceLocator
import pytest


@pytest.fixture
def mock_services() -> Generator[MockServiceLocator, None, None]:
    original_service_locator = get_service_locator()
    mock_service_locator = MockServiceLocator()
    set_service_locator(mock_service_locator)

    yield mock_service_locator

    set_service_locator(original_service_locator)


@pytest.fixture
def mock_time_service(
    mock_services: MockServiceLocator,
) -> MockTimeService:
    return mock_services.mock_time_service
