import logging
import os
import firebase_admin
from hackathon.settings import BASE_DIR
from infrastructure.logging.actions import log_error, log_event
from firebase_admin import credentials, messaging

from infrastructure.service_locator.push_notifications.push_notification_service import (
    PushNotification,
    PushNotificationService,
    Token,
    TokenExpiredError,
)
from infrastructure.viewer_context.viewer_context import AnonymousViewerContext


class FirebaseNotificationService(PushNotificationService):
    def __init__(self) -> None:
        certificate_path = os.path.join(BASE_DIR, "firebase_certificate.json")
        try:
            cred = credentials.Certificate(certificate_path)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            log_error(None, "firebase_notification_service", "init", {}, e)

    def send_notification(self, token: Token, notification: PushNotification) -> None:
        data = notification.data
        data["type"] = notification.type
        message = messaging.Message(
            notification=messaging.Notification(
                title=notification.title,
                body=notification.subtitle,
                image=notification.profile_pic_url,
            ),
            apns=messaging.APNSConfig(
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(
                        alert=messaging.ApsAlert(
                            title=notification.title, body=notification.subtitle
                        ),
                        sound="default",
                        mutable_content=True,
                        badge=notification.badge if notification.badge > 0 else None,
                    ),
                    data=data,
                ),
                fcm_options=messaging.APNSFCMOptions(
                    image=notification.profile_pic_url,
                ),
            ),
            token=token.token,
            data=data,
        )
        try:
            messaging.send(message)
            log_event(
                AnonymousViewerContext(),
                "firebase_notification_service",
                "send_notification",
                {
                    "token": token.token,
                    "notification": notification,
                },
            )
        except messaging.UnregisteredError:
            raise TokenExpiredError(token)
        except Exception as e:
            log_error(
                None,
                "firebase_notification_service",
                "send_notification",
                {
                    "token": token.token,
                    "notification": notification,
                },
                e,
            )
