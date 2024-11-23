import datetime
from infrastructure.service_locator.geolocation_service import (
    Coordinates,
    GeocodingService,
)
from infrastructure.service_locator.predition_service import PredictionService
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
