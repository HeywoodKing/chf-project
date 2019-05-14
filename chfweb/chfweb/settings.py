"""
Django settings for chfweb project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rnx96978^u&3g*e12j7rt-b@-95rj+=(bl791)(^gllw$j(-nl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.4.30', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'chinslicking',
    'chinslicking.templatetags',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # 添加此行
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chfweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'chinslicking', 'templates'),
            os.path.join(BASE_DIR, 'home', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 添加这一行，可以理解为中间件的意思
                # 'django.template.context_processors.uploads',
                'home.views.global_setting',
                'chinslicking.views.global_setting',
            ],
        },
    },
]

WSGI_APPLICATION = 'chfweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'chf',
        'USER': 'root',
        'PASSWORD': '123456'
    }
}

# DATABASES_APPS_MAPPING = {
#     # 'app':'default',
#     'home':'mysqldb',
# }

# DATABASE_ROUTERS = ['blog.database_app.router.DatabaseAppsRouter']


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('zh-Hans', _('中文简体')),
    ('zh-Hant', _('中文繁體')),
)

# 翻译文件所在目录，需要手工创建
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'home', 'static'),
    os.path.join(BASE_DIR, 'chinslicking', 'static'),
)

# 自定义用户model 否则会报：HINT: Add or change a related_name argument to the definition for ‘User.user_permissions’ or ‘User.user_permissions’.
AUTH_USER_MODEL = 'home.User'

SITE_NAME = '春和方'
SITE_DESC = 'CHF官网'
SITE_AUTHOR = 'flack'

SITE_NAME2 = '秦食皇'
SITE_DESC2 = '秦食皇官网'
SITE_AUTHOR2 = 'flack'


MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads').replace('\\', '/')  #设置静态文件路径为主目录下的uploads文件夹

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'fotmat': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'  #日志格式
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'home.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
        # 'require_debug_true': {
        #     '()': 'django.utils.log.RequireDebugTrue'
        # }
    },
    'handlers': {
        # 'default': {
        #     'level':'DEBUG',
        #     'class':'logging.handlers.RotatingFileHandler',
        #     'filename': 'log/all.log',                #日志输出文件
        #     'maxBytes': 1024*1024*5,                  #文件大小
        #     'backupCount': 2,                         #备份份数
        #     'formatter':'standard',                   #使用哪种formatters日志格式
        # },
        # 'error': {
        #     'level':'ERROR',
        #     'class':'logging.handlers.RotatingFileHandler',
        #     'filename': 'log/error.log',
        #     'maxBytes':1024*1024*5,
        #     'backupCount': 2,
        #     'formatter':'standard',
        # },
        # 'file': {
        #     'level': 'ERROR',
        #     'class': 'logging.FileHandler',
        #     'filename': 'log/error.log',
        #     'formatter': 'verbose',
        #     # 'filters': ['require_debug_true'],
        # },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            # 'filters': ['require_debug_true'],
        },
        'null': {
            'class': 'logging.NullHandler',
        }
    },
    'loggers': {
        # 'django': {
        #     'handlers': ['console'],
        #     'level': 'info',
        #     'propagate': True,
        # },
        # 'django.request': {
        #     'handlers': ['file'],
        #     'level': 'ERROR',
        #     'propagate': False
        # },
    },
}
