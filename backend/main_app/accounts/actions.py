from typing import Optional
from infrastructure.viewer_context.viewer_context import ViewerContext
from main_app.accounts.models import User, get_username_from_email
from django.contrib.auth import authenticate as django_authentication
from rest_framework.authtoken.models import Token
from infrastructure.privacy_rules.privacy_rules import is_same_user


class UserAlreadyExists(Exception):
    def __init__(self) -> None:
        super().__init__("User already exists")


class WrongEmailOrPassword(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid email or password")


def create_user(
    viewer_context: ViewerContext,
    name: str,
    email: str,
    password: str,
) -> User:
    if User.objects.filter(email=email).exists():
        raise UserAlreadyExists()
    return User.objects.create_user(
        name=name,
        email=email,
        password=password,
    )


def create_user_token(
    viewer_context: ViewerContext, email: str, password: Optional[str]
) -> str:
    if not django_authentication(
        username=get_username_from_email(email), password=password
    ):
        raise WrongEmailOrPassword()

    user = User.objects.get(email=email)

    token, _ = Token.objects.get_or_create(user=user)

    return str(token.key)


@is_same_user()
def rename_user(viewer_context: ViewerContext, user: User, name: str) -> User:
    user.name = name
    user.save()
    return user
