from infrastructure.privacy_rules.privacy_rules import is_authenticated
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.parkings.models import Parking


def get_parking_by_id(viewer_context: ViewerContext, parking_id: str) -> Parking:
    try:
        return Parking.objects.get(unique_id=parking_id)
    except Parking.DoesNotExist:
        raise ValueError("Parking not found")


def get_all_parkings(viewer_context: ViewerContext) -> list[Parking]:
    return list(Parking.objects.all())
