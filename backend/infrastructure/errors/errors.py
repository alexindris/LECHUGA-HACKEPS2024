from django.utils.translation import gettext as _


class NotAuthorizedActionError(Exception):
    def __init__(self) -> None:
        super().__init__(_("Error message: Not permited"))


class NotValidActionError(Exception):
    reason: str

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(_(reason))


class ParameterTypeError(Exception):
    def __init__(self, name: str, expected_type: type) -> None:
        super().__init__(f"{name} must be {expected_type.__name__}")


class MissingParameterError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is required")
