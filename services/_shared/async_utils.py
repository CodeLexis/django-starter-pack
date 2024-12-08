from functools import wraps
from celery import shared_task
from django.conf import settings

from project import logger


def background_task(func):
    # Register the task with Celery
    task = shared_task(func)

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if settings.IS_TESTING:
            logger.info(f"Running background task {func.__name__}(...) synchronously for {'- test' if settings.IS_TESTING else ''} {'- hydration' if settings.IS_HYDRATING else ''}...")
            # Run the task synchronously
            return func(*args, **kwargs)
        else:
            # Run the task asynchronously using Celery
            return task.delay(*args, **kwargs)

    return wrapped_func