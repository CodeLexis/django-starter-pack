from uuid import uuid4
from django.db import models

from .fields import STATUS_FIELD
from .managers import BaseManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    guid = models.CharField(default=uuid4, max_length=36, primary_key=True)
    is_deleted = models.BooleanField(default=False)
    metadata = models.JSONField(blank=True, default=dict, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = STATUS_FIELD()

    objects = BaseManager()

    class Meta:
        abstract = True

    def __str__(self):
        return getattr(self, 'name', str(self.guid))

    def delete(self):
        """Mark the record as deleted instead of deleting it"""
        if hasattr(self, 'name'):
            self.name = f'DELETED <{self.guid}>'

        self.is_deleted = True
        self.save()
