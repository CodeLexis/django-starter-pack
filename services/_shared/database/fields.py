from django.db import models

from services._shared.third_party.storage.azure import CustomAzureStorage


IMAGE_FIELD = lambda *args, **kwargs: models.ImageField(*args, **kwargs, blank=True, null=True, storage=CustomAzureStorage())
MANY_TO_MANY_FIELD = lambda *args, **kwargs: models.ManyToManyField(*args, **kwargs)
MANY_TO_ONE_FIELD = lambda *args, **kwargs: models.ForeignKey(*args, on_delete=models.CASCADE, **kwargs)
NAME_FIELD = lambda *args, **kwargs: models.CharField(max_length=24, *args, **kwargs)
ONE_TO_ONE_FIELD = lambda *args, **kwargs: models.OneToOneField(*args, on_delete=models.CASCADE, **kwargs)
STATUS_FIELD = lambda default='ACTIVE', *args, **kwargs: models.CharField(
    *args,
    choices=[
        ('ACTIVE', 'Active'),
        ('CANCELLED', 'Cancelled'),
        ('FAILED', 'Failed'),
        ('HIDDEN', 'Hidden'),
        ('INACTIVE', 'Inactive'),
        ('NEW', 'New'),
        ('PROCESSED', 'Processed'),
        ('SENT', 'Sent'),
        ('STARTED', 'Started'),
        ('SUCCESSFUL', 'Successful'),
    ],
    default=default,
    max_length=32,
    **kwargs)