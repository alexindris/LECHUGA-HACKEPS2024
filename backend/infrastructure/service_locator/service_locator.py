from abc import ABC, abstractmethod
import importlib
import os
from pathlib import Path
from typing import Optional

from infrastructure.service_locator.geolocation_service import (
    GeocodingService,
    NomatimGeocodingService,
)
from infrastructure.service_locator.predition_service import (
    ParkingPredictionService,
    PredictionService,
)
from infrastructure.service_locator.time_service import SystemTimeService, TimeService


class ServiceLocatorBase(ABC):
    @abstractmethod
    def timeService(self) -> TimeService:
        pass

    @abstractmethod
    def geolocationService(self) -> GeocodingService:
        pass

    @abstractmethod
    def predictionService(self) -> PredictionService:
        pass


class ServiceLocator(ServiceLocatorBase):
    time_service: TimeService
    geocoding_service: GeocodingService
    prediction_service: PredictionService

    def __init__(self) -> None:
        self.geocoding_service = NomatimGeocodingService()
        self.time_service = SystemTimeService()
        self.prediction_service = ParkingPredictionService()

    def timeService(self) -> TimeService:
        return self.time_service

    def geolocationService(self) -> GeocodingService:
        return self.geocoding_service

    def predictionService(self) -> PredictionService:
        return self.prediction_service


service_locator: Optional[ServiceLocatorBase] = None


def set_service_locator(new_service_locator: ServiceLocatorBase) -> None:
    global service_locator
    service_locator = new_service_locator


def get_service_locator() -> ServiceLocatorBase:
    global service_locator
    if service_locator is None:
        set_service_locator(ServiceLocator())

    if service_locator is None:
        raise Exception("Service locator not set")

    return service_locator


def find_subscriptions_in_path(path: Path) -> None:
    for root, dirs, files in os.walk(path):
        if "subscriptions.py" in files:
            module_name = os.path.relpath(os.path.join(root, "subscriptions")).replace(
                os.sep, "."
            )
            importlib.import_module(module_name)
