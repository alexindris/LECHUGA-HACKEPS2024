from typing import Any, Optional
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager["User"]):
    def create_user(
        self,
        name: str,
        email: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> "User":
        if not username:
            username = get_username_from_email(email)

        user = self.model(
            name=name,
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: str,
        password: str,
        email: Optional[str] = None,
    ) -> "User":
        user = self.create_user(
            name=username,
            username=username,
            email=email or f"{username}@admin.com",
            password=password,
        )
        user.is_admin = True


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm: Any, obj: Any = None) -> bool:
        return True

    def has_module_perms(self, app_label: str) -> bool:
        return True


def get_username_from_email(email: str) -> str:
    return "".join(email.split("@")).lower().replace(".", "")
