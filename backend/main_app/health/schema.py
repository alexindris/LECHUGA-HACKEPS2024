from django.db import connection
import graphene

from infrastructure.service_locator.service_locator import get_service_locator


class HealthType(graphene.ObjectType):
    status = graphene.String(required=True)
    time = graphene.DateTime(required=True)

    @staticmethod
    def get_health():
        try:
            connection.ensure_connection()
            return HealthType(
                status="ok",
                time=get_service_locator().timeService().getCurrentTime(),
            )
        except Exception:
            return HealthType(
                status="error",
                time=get_service_locator().timeService().getCurrentTime(),
            )
