import datetime
from abc import ABC, abstractmethod


class PredictionService(ABC):
    @abstractmethod
    def predict_parking(self, date: datetime.datetime) -> int:
        raise NotImplementedError()


class ParkingPredictionService(PredictionService):
    def predict_parking(self, date: datetime.datetime) -> int:
        return 0
