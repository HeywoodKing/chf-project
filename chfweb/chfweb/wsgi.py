"""
WSGI config for chfweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings')

env = os.environ.get('DJANGO_SETTINGS_PROFILE', 'pro')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings.%s' % env)
os.environ['DJANGO_SETTINGS_MODULE'] = 'chfweb.settings.%s' % env

application = get_wsgi_application()

