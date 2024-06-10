from uuid import uuid4

from django.db import models


class BaseQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_deleted=True)

    def for_any_tenant(self, tenants):
        return self.filter(tenant__in=tenants)

    def for_tenant(self, tenant):
        return self.filter(tenant=tenant)


class UserQuerySet(BaseQuerySet):
    def delete(self):
        self.update(username=f'<DELETED: {uuid4()}>', is_active=False)

        super().delete()
