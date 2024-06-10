from django.contrib import admin

from services._shared.admin import BaseModelAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseModelAdmin):
    list_display = ('username', 'email', 'guid', 'joined_at', 'created_at', 'modified_at')
