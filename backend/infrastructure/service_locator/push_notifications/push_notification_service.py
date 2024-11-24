from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class PushNotification:
    type: str = ""
    title: str = "Title"
    subtitle: str = ""
    profile_pic_url: Optional[str] = None
    data: dict[str, Any] = field(default_factory=dict)
    badge: int = 0


@dataclass
class Token:
    token: str


class TokenExpiredError(Exception):
    def __init__(self, token: Token) -> None:
        super().__init__(f"Token {token.token} has expired")


class PushNotificationService(ABC):
    @abstractmethod
    def send_notification(self, token: Token, notification: PushNotification) -> None:
        pass
