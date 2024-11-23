import sys
from django.apps import AppConfig


class HackAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    def ready(self) -> None:
        if "runserver" in sys.argv:
            from main_app.parkings.mqtt import start_mqtt

            start_mqtt()
