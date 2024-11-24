import datetime
from typing import List
from infrastructure.service_locator.geolocation_service import (
    Coordinates,
    GeocodingService,
)
from infrastructure.service_locator.predition_service import PredictionService
from infrastructure.service_locator.push_notifications.push_notification_service import (
    PushNotification,
    PushNotificationService,
    Token,
    TokenExpiredError,
)
from infrastructure.service_locator.time_service import TimeService


class MockTimeService(TimeService):
    current_time: datetime.datetime = datetime.datetime(
        2021, 7, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
    )

    def getCurrentTime(self) -> datetime.datetime:
        return self.current_time

    def set_current_time(self, current_time: datetime.datetime) -> None:
        self.current_time = current_time

    def advance_time(self, seconds: int) -> datetime.datetime:
        self.current_time += datetime.timedelta(seconds=seconds)
        return self.current_time


class MockGeoCodingService(GeocodingService):
    def get_coordinates(self, address: str) -> Coordinates:
        return Coordinates("0", "0")


class MockPredictionService(PredictionService):
    prediction = 0

    def predict_parking(self, date: datetime.datetime) -> int:
        return self.prediction

    def set_prediction(self, prediction: int) -> None:
        self.prediction = prediction
class MockPushNotificationService(PushNotificationService):
    sent_notifications: dict[str, List[PushNotification]]
    sent_data_messages: dict[str, List[PushNotification]]
    expired_tokens: List[str]

    def __init__(self) -> None:
        self.sent_notifications = {}
        self.expired_tokens = []
        self.sent_data_messages = {}

    def clear(self) -> None:
        self.sent_notifications = {}
        self.expired_tokens = []
        self.sent_data_messages = {}

    def send_notification(self, token: Token, notification: PushNotification) -> None:
        for key in notification.data:
            if not isinstance(notification.data[key], str):
                raise ValueError(f"Data for key {key} is not a string")

        if token.token not in self.sent_notifications:
            self.sent_notifications[token.token] = []

        self.sent_notifications[token.token].append(notification)
        if token.token in self.expired_tokens:
            raise TokenExpiredError(token)

    def add_expired_token(self, token: str) -> None:
        self.expired_tokens.append(token)
