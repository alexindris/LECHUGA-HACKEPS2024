from infrastructure.service_locator.mock_services import MockTimeService
from infrastructure.service_locator.service_locator import ServiceLocatorBase
from infrastructure.service_locator.time_service import TimeService


class MockServiceLocator(ServiceLocatorBase):
    mock_time_service: MockTimeService

    def __init__(self) -> None:
        self.mock_time_service = MockTimeService()

    def timeService(self) -> TimeService:
        return self.mock_time_service
