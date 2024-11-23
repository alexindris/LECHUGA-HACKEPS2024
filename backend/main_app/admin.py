from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from main_app.accounts.models import User


class UserAdmin(BaseUserAdmin):
    model = User  # type: ignore
    list_display = ("username", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_admin",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
