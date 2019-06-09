"""
WSGI config for chfweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

import sys
sys.path.insert(0, PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
