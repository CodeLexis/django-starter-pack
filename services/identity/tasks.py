from celery import shared_task

from .models import User


@shared_task
def set_user_password_task(user_guid: str, password: str) -> User:
    user = User.objects.get(guid=user_guid)
    user.set_password(password)
    user.save()
