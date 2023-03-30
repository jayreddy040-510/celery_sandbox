from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_sandbox.settings')

app = Celery('celery_sandbox')
app.conf.enable_utc = False

app.conf.update(timezone = 'America/Los_Angeles')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
