import os

from celery import Celery

from LMA.settings import base

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LMA.settings.development")
# Tell Celery to retry connecting to the broker on startup
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
broker_connection_retry_on_startup = True
app = Celery("real_estate", broker="redis://redis:6379/0")


app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
