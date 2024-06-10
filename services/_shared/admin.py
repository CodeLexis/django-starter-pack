from django.contrib import admin


DEFAULT_READONLY_FIELDS = ['guid', 'created_at', 'modified_at']


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = DEFAULT_READONLY_FIELDS
