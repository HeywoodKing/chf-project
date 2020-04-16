#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings')
    env = os.environ.get('DJANGO_SETTINGS_PROFILE', 'dev')
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings.%s' % env)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'chfweb.settings.%s' % env

=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings')
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chfweb.settings.local')
>>>>>>> 12d4e38c285f084c80306a400786e3e701b9a075
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
