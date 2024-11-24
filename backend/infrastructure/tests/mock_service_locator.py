from infrastructure.service_locator.geolocation_service import GeocodingService
from infrastructure.service_locator.mock_services import (
    MockGeoCodingService,
    MockPredictionService,
    MockPushNotificationService,
    MockTimeService,
)
from infrastructure.service_locator.predition_service import PredictionService
from infrastructure.service_locator.service_locator import ServiceLocatorBase
from infrastructure.service_locator.time_service import TimeService


class MockServiceLocator(ServiceLocatorBase):
    mock_time_service: MockTimeService
    mock_geocoding_service: MockGeoCodingService
    mock_prediction_service: MockPredictionService
    mock_push_notification_service: MockPushNotificationService

    def __init__(self) -> None:
        self.mock_time_service = MockTimeService()
        self.mock_geocoding_service = MockGeoCodingService()
        self.mock_prediction_service = MockPredictionService()
        self.mock_push_notification_service = MockPushNotificationService()

    def timeService(self) -> TimeService:
        return self.mock_time_service

    def geolocationService(self) -> GeocodingService:
        return self.mock_geocoding_service

    def predictionService(self) -> PredictionService:
        return self.mock_prediction_service
    def pushNotificationService(self) -> MockPushNotificationService:
        return self.mock_push_notification_service
