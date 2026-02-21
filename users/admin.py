from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "telegram_chat_id")
    fields = (
        "email",
        "phone",
        "city",
        "avatar",
        "telegram_chat_id",
        "is_active",
        "is_staff",
    )
