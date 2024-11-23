from abc import ABC, abstractmethod
from dataclasses import dataclass
from geopy.geocoders import Nominatim


@dataclass
class Coordinates:
    latitude: str
    longitude: str


class GeocodingService(ABC):

    @abstractmethod
    def get_coordinates(self, address: str) -> Coordinates:
        raise NotImplementedError()


class NomatimGeocodingService(GeocodingService):
    def get_coordinates(self, address: str) -> Coordinates:
        geolocator = Nominatim(user_agent="parking-app")
        location = geolocator.geocode(address)
        return Coordinates(location.latitude, location.longitude)
