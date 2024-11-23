from infrastructure.privacy_rules.privacy_rules import is_authenticated
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.parkings.getter import get_parking_by_id
from main_app.parkings.models import EntryType, Parking, ParkingEntry


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


@is_authenticated
def create_parking_entry(
    viewer_context: ViewerContext, parkin_id: str, entry_type: EntryType
) -> ParkingEntry:

    parking = get_parking_by_id(viewer_context, parkin_id)

    if entry_type == EntryType.ENTRANCE:
        parking.occupied_lots += 1
    else:
        parking.occupied_lots -= 1

    parking.save()

    return ParkingEntry.objects.create(parking=parking, entry_type=entry_type)
