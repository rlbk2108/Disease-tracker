import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Disease_Tracker.settings")
app = Celery("Disease_Tracker")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()