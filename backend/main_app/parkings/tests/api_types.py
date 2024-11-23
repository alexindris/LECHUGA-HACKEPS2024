from dataclasses import dataclass


@dataclass
class ParkingEntry:
    entryType: str
    createdAt: str


@dataclass
class ParkingType:
    identifier: str
    name: str
    address: str
    totalLots: int
    occupiedLots: int
    entries: list[ParkingEntry]
