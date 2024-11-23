import pytest

from typing import Generator

from infrastructure.tests.mock_service_locator import MockServiceLocator

from infrastructure.tests.mock_fixtures import *
from infrastructure.viewer_context.tests.fixtures import *


@pytest.fixture(autouse=True)
def mock_for_all_test(
    mock_services: MockServiceLocator,
    request: pytest.FixtureRequest,
) -> Generator[None, None, None]:
    if "logic" in request.keywords or "view" in request.keywords:
        request.getfixturevalue("all_powerful_viewer_context")
    yield
