from infrastructure.privacy_rules.privacy_rules import is_authenticated
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.parkings.models import Parking


@is_authenticated
def get_parking_by_id(viewer_context: ViewerContext, parking_id: str) -> Parking:
    try:
        return Parking.objects.get(unique_id=parking_id)
    except Parking.DoesNotExist:
        raise ValueError("Parking not found")
