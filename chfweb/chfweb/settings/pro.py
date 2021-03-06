import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '172.16.40.247',
    '47.99.121.101',
    'www.xaqsh.cn',
    'www.xaqsh.com',
    'www.xianqinshihuang.com',
    'www.xachf.com',
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

HOST = os.environ.get('MYSQL_HOST', '127.0.0.1')
PORT = os.environ.get('MYSQL_PORT', '3306')
USER = os.environ.get('MYSQL_USER', None)
PASS = os.environ.get('MYSQL_PASS', None)
NAME = os.environ.get('MYSQL_DB', 'chf')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASS,
        'OPTIONS': {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
