from dataclasses import dataclass


@dataclass
class ParkingType:
    identifier: str
    name: str
    address: str
    totalLots: int
    occupiedLots: int
