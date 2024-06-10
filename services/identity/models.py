from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from services._shared.database.fields import IMAGE_FIELD
from services._shared.database.managers import UserManager
from services._shared.database.model import BaseModel


class User(BaseModel, AbstractUser):
    avatar = IMAGE_FIELD()
    joined_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    class Meta:
        db_table = 'identity.users'
