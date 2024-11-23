from infrastructure.privacy_rules.privacy_rules import is_authenticated
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.parkings.getter import get_parking_by_id
from main_app.parkings.models import Parking, ParkingEntry


@is_authenticated
def create_parking(
    viewer_context: ViewerContext, name: str, address: str, total_lots: int
) -> Parking:
    if not name:
        raise ValueError("Name cannot be empty")

    if not address:
        raise ValueError("Address cannot be empty")

    if total_lots <= 0:
        raise ValueError("Total lots must be greater than 0")

    return Parking.objects.create(
        name=name,
        address=address,
        total_lots=total_lots,
    )
