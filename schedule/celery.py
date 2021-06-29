from __future__ import absolute_import, unicode_literals

import os
from dotenv import load_dotenv

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schedule.settings')

app = Celery('schedule')

app.config_from_object('django.conf:settings', namespace='CELERY')

try:
    load_dotenv(verbose=True)
except Exception as ex:
    raise ImportError(
        "couldn't import env file.Error:"+str(ex)
    )

app.conf.BROKER_URL = os.getenv("broker_url")
app.conf.result_backend = os.getenv("result_backend")
app.conf.accept_content = os.getenv("accept_content").split(",")
app.conf.task_serializer = os.getenv("task_serializer")
app.conf.result_serializer = os.getenv("result_serializer")
app.conf.timezone = os.getenv("timezone")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))