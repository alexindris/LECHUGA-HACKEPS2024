from django.db import models

from hackathon import settings


class Device(models.Model):
    push_token = models.CharField(max_length=255)
