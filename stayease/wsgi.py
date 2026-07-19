"""
WSGI config for stayease project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stayease.settings')

# Run migrations on startup if DATABASE_URL is set (production)
if os.environ.get('DATABASE_URL'):
    try:
        sys.argv = ['manage.py', 'migrate', '--noinput']
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Migration error: {e}")

application = get_wsgi_application()
