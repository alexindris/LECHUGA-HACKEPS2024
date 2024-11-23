import uuid
from django.db import models


class EntryType(models.TextChoices):
    ENTRANCE = "EN"
    EXIT = "EX"


class Parking(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    total_lots = models.IntegerField(null=False, blank=False)
    occupied_lots = models.IntegerField(default=0)
    latitude = models.CharField(max_length=100, null=False, blank=False, default="0")
    longitude = models.CharField(max_length=100, null=False, blank=False, default="0")

    def __str__(self) -> str:
        return self.name

    def get_entries(self) -> list["ParkingEntry"]:
        return list(self.parkingentry_set.all())


class ParkingEntry(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=2, choices=EntryType.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.parking.name} - {self.entry_type}"
