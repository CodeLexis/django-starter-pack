from __future__ import absolute_import, unicode_literals

from celery import Celery
import os

from . import logger


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    logger.info(f'Request: {self.request!r}')
