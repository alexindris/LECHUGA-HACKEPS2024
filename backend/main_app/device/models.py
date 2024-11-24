from django.db import models

from hackathon import settings


class Device(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="devices",
    )

    push_token = models.CharField(max_length=255)
