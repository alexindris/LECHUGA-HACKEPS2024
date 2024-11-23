from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional
from infrastructure.errors.errors import NotAuthorizedActionError

if TYPE_CHECKING:
    from main_app.accounts.models import User


class NotIdentifiedViewerContextError(Exception):
    def __init__(self) -> None:
        super().__init__("Viewer context is not identified")


class ViewerContext(ABC):
    @abstractmethod
    def is_authenticated(self) -> bool:
        pass

    @abstractmethod
    def is_identified(self) -> bool:
        pass

    @abstractmethod
    def identified_user(self) -> "User":
        pass

    @abstractmethod
    def is_all_powerful(self) -> bool:
        pass


class UserViewerContext(ViewerContext):
    def __init__(
        self,
        user: "User",
    ):
        self.user = user

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, UserViewerContext):
            return False

        return self.user == value.user

    def is_authenticated(self) -> bool:
        return True

    def is_identified(self) -> bool:
        return True

    def identified_user(self) -> "User":
        return self.user

    def is_all_powerful(self) -> bool:
        return False


class AnonymousViewerContext(ViewerContext):
    def __eq__(self, value: object) -> bool:
        return isinstance(value, AnonymousViewerContext)

    def is_authenticated(self) -> bool:
        return False

    def is_identified(self) -> bool:
        return False

    def identified_user(self) -> "User":
        raise NotAuthorizedActionError()

    def is_all_powerful(self) -> bool:
        return False


class AllPowerfulViewerContext(ViewerContext):
    def __init__(self, user: Optional["User"]) -> None:
        self.user = user

    def __eq__(self, value: object) -> bool:
        return isinstance(value, AllPowerfulViewerContext)

    def is_authenticated(self) -> bool:
        return True

    def is_identified(self) -> bool:
        return self.user is not None

    def identified_user(self) -> "User":
        if self.user is None:
            raise NotIdentifiedViewerContextError()
        return self.user

    def is_all_powerful(self) -> bool:
        return True
