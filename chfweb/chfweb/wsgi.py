"""
WSGI config for chfweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings')

env = os.environ.get('DJANGO_SETTINGS_PROFILE', 'pro')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings.%s' % env)
os.environ['DJANGO_SETTINGS_MODULE'] = 'chfweb.settings.%s' % env
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings.production')
>>>>>>> 12d4e38c285f084c80306a400786e3e701b9a075

application = get_wsgi_application()
