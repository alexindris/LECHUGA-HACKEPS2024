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
    available_lots = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ParkingEntry(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=2, choices=EntryType.choices)

    def __str__(self):
        return f"{self.parking.name} - {self.entry_type}"
