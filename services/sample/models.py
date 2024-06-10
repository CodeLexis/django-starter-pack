from django.db import models

from services._shared.database.model import BaseModel


class Message(BaseModel):
    content = models.CharField(max_length=16)


# Add models here
