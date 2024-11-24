from infrastructure.privacy_rules.privacy_rules import is_same_user
from infrastructure.service_locator.push_notifications.push_notification_service import (
    PushNotification,
    Token,
    TokenExpiredError,
)
from infrastructure.service_locator.service_locator import get_service_locator
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.accounts.models import User
from main_app.device.models import Device


def send_notification(
    viewer_context: ViewerContext,
    notification: PushNotification,
) -> None:
    all_devices = Device.objects.all()
    for device in all_devices:
        try:
            get_service_locator().pushNotificationService().send_notification(
                Token(device.push_token),
                notification,
            )
        except TokenExpiredError:
            _unregister_device(viewer_context, device.push_token)


def _unregister_device(
    viewer_context: ViewerContext,
    push_token: str,
) -> None:
    devices = Device.objects.filter(push_token=push_token).all()

    for device in devices:
        device.delete()


def register_device(
    viewer_context: ViewerContext,
    push_token: str,
) -> None:
    devices = Device.objects.filter(push_token=push_token).all()

    for device in devices:
        device.delete()

    Device.objects.create(push_token=push_token)
