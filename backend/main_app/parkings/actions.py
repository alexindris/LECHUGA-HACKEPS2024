from infrastructure.privacy_rules.privacy_rules import is_authenticated
from infrastructure.service_locator.service_locator import get_service_locator
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.parkings.getter import get_parking_by_id
from main_app.parkings.models import EntryType, Parking, ParkingEntry
from django.db import transaction
from main_app.device.action import send_notification
from infrastructure.service_locator.push_notifications.push_notification_service import (
    PushNotification,
)

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

    coordinates = get_service_locator().geolocationService().get_coordinates(address)
    return Parking.objects.create(
        name=name,
        address=address,
        total_lots=total_lots,
        latitude=coordinates.latitude,
        longitude=coordinates.longitude,
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

    if parking.occupied_lots < 0:
        raise ValueError("Parking is empty")

    if parking.occupied_lots > parking.total_lots:
        raise ValueError("Parking is full")
    
    if parking.occupied_lots == parking.total_lots:
        send_notification(
            viewer_context,
            PushNotification(
                type="parking_full",
                title="Parking full",
                subtitle=f"Parking {parking.name} is full",
            ),
        )
    elif entry_type == EntryType.EXIT:
        send_notification(
            viewer_context,
            PushNotification(
                type="new_spot_available",
                title="New spot available",
                subtitle=f"Parking {parking.name} has new spot available",             
            ),
        )


    with transaction.atomic():
        parking.save()
        return ParkingEntry.objects.create(parking=parking, entry_type=entry_type)
