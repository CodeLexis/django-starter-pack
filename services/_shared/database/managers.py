from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models
from django.db.models.signals import post_save

from .querysets import BaseQuerySet, UserQuerySet


class BaseManager(models.Manager):
    def bulk_create(self, created_objects, **kwargs):
        for obj in created_objects:
            post_save.send(
                sender=self.model,
                instance=obj,
                created=True,
                using=kwargs.get('using'),
                update_fields=kwargs.get('update_fields')
            )

        return super(BaseManager, self).bulk_create(created_objects, **kwargs)  

    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db).exclude(is_deleted=True)


class UserManager(BaseUserManager):
    def for_group(self, name: str):
        return self.get_queryset().filter(groups__name=name)
    
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db).prefetch_related('groups').exclude(is_deleted=True)
