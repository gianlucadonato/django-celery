from __future__ import absolute_import
from django.conf import settings
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eversnap_project.settings')

app = Celery('eversnap_project')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# NOTE:
# ==========================================
# SHELL COMMAND:
# python manage.py celeryd -B -l info
# or
# python manage.py celery worker -B -l info
# 
# Starts celery and celeybeat deamon.
# The -l info asks the workers to log every message with a priority >= to "info"
# ===========================================
