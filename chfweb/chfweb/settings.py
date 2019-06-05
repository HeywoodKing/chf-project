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

ALLOWED_HOSTS = ['192.168.4.30', '192.168.0.100', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
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

USE_TZ = False

LANGUAGES = (
    ('zh-hans', _('中文简体')),
    ('en', _('English')),
    # ('zh-Hant', _('中文繁體')),
)

LANGUAGES_SUPPORTED = ('en', 'zh-hans', )



# 翻译文件所在目录，需要手工创建
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.core.context_processors.i18n',
# )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# 如果不设置STATIC_ROOT这个参数，使用django-jet美化后台python manage.py collectstatic 会报错
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'home', 'static'),
    os.path.join(BASE_DIR, 'chinslicking', 'static'),
)


# 自定义用户model 否则会报：HINT: Add or change a related_name argument to the definition
# for ‘User.user_permissions’ or ‘User.user_permissions’.
AUTH_USER_MODEL = 'home.ChfUserProfile'

SITE_NAME = '春和方'
SITE_DESC = '春和方官网'
SITE_AUTHOR = 'flack'

SITE_NAME2 = '秦食皇'
SITE_DESC2 = '秦食皇官网'
SITE_AUTHOR2 = 'flack'


MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads').replace('\\', '/')  # 设置静态文件路径为主目录下的uploads文件夹

# django-jet
JET_DEFAULT_THEME = 'default'
# default green light-violet light-green light-blue light-gray
# JET_THEMES = [
#     {
#         'theme': 'default', # theme folder name
#         'color': '#47bac1', # color of the theme's button in user menu
#         'title': 'Default' # theme title
#     },
#     {
#         'theme': 'green',
#         'color': '#44b78b',
#         'title': 'Green'
#     },
#     {
#         'theme': 'light-green',
#         'color': '#2faa60',
#         'title': 'Light Green'
#     },
#     {
#         'theme': 'light-violet',
#         'color': '#a464c4',
#         'title': 'Light Violet'
#     },
#     {
#         'theme': 'light-blue',
#         'color': '#5EADDE',
#         'title': 'Light Blue'
#     },
#     {
#         'theme': 'light-gray',
#         'color': '#222',
#         'title': 'Light Gray'
#     }
# ]

# 上下最近的导航，默认True
# JET_CHANGE_FORM_SIBLING_LINKS = True

# 侧边栏压缩
JET_SIDE_MENU_COMPACT = False

# A list of application or custom item dicts
# 多站点管理
# JET_SIDE_MENU_ITEMS = {
#     'system': [
#         {
#             'label': _('系统'),
#             'app_label': 'home',
#             'items': []
#         }
#     ],
#     'descr_manager': [
#         {
#             'label': _('简介管理'),
#             'app_label': 'home',
#             'items': [
#                 {
#                     'name': 'ChfAbout',
#                     'label': _('品牌介绍'),
#                     'url': '',
#                 },
#                 {'name': 'ChfAboutResource', 'label': _('品牌介绍图片资源')},
#                 {'name': 'ChfCompanyHistory', 'label': _('发展历程'), 'url': 'http://example.com', 'url_blank': True},
#             ]
#         }
#     ],
#     'user_manager': [
#         {
#             'label': _('管理员管理'),
#             'items': [
#                 {'name': 'core.user'},
#                 {'name': 'auth.group'},
#                 {'name': 'core.userprofile', 'permissions': ['core.user']},
#             ]
#         }
#     ]
# }
JET_SIDE_MENU_ITEMS = [
    {
        'label': _('系统'),
        'app_label': 'sys',
        'items': [
            {'name': 'SysClearCache', 'label': _('清除系统缓存')},
            {'name': 'SysLoginLog', 'label': _('管理员登录情况')},
            {'name': 'SysDbBackup', 'label': _('数据库备份')},
            {'name': 'SysKeyWords', 'label': _('关键词管理')},
        ]
    },
    {
        'label': _('信息管理'),
        'app_label': 'info',
        'items': [
            {'name': 'ChfIndexPlate', 'label': _('首页模块'), 'url': '/admin/home/chfindexplate/', 'url_blank': False},
            {'name': 'ChfUserWateringRecord', 'label': _('用户浇水记录'), 'url': '/admin/home/chfuserwateringrecord/', 'url_blank': False},
            {'name': 'ChfApplyRecord', 'label': _('用户抢券记录'), 'url': '/admin/home/chfapplyrecord/', 'url_blank': False},
            {'name': 'ChfWateringQty', 'label': _('浇水水量余额'), 'url': '/admin/home/chfwateringqty/', 'url_blank': False},
            {'name': 'ChfNews', 'label': _('新闻资讯'), 'url': '/admin/home/chfnews/', 'url_blank': False},
            {'name': 'ChfPartner', 'label': _('品牌合作'), 'url': '/admin/home/chfpartner/', 'url_blank': False},
            {'name': 'ChfAnimateType', 'label': _('动画类型'), 'url': '/admin/home/chfanimatetype/', 'url_blank': False},
            # {
            #     'name': 'ChfAnimateType',
            #     'label': _('动画类型000'),
            #     'items': [
            #         {'name': 'ChfPartner', 'label': _('品牌合作111')},
            #         {'name': 'ChfAnimateType', 'label': _('动画类型222')},
            #     ]
            # },
        ]
    },
    {
        'label': _('产品管理'),
        'app_label': 'product',
        'items': [
            {'name': 'ChfProduct', 'label': _('产品管理'), 'url': '/admin/home/chfproduct/', 'url_blank': False},
            {'name': 'ChfProductType', 'label': _('产品类型'), 'url': '/admin/home/chfproducttype/', 'url_blank': False},
        ]
    },
    {
        'label': _('简介管理'),
        'app_label': 'breif',
        'items': [
            {'name': 'ChfAbout', 'label': _('品牌介绍'), 'url': '/admin/home/chfabout/', 'url_blank': False},
            {'name': 'ChfAboutResource', 'label': _('品牌介绍图片资源'), 'url': '/admin/home/chfaboutresource/', 'url_blank': False},
            {'name': 'ChfCompanyHistory', 'label': _('发展历程'), 'url': '/admin/home/chfcompanyhistory/', 'url_blank': False},
        ]
    },
    {
        'label': _('留言管理'),
        'app_label': 'message',
        'items': []
    },
    {
        'label': _('招聘管理'),
        'app_label': 'job',
        'items': [
            {'name': 'ChfJobRecruit', 'label': _('工作机会'), 'url': '/admin/home/chfjobrecruit/', 'url_blank': False},
        ]
    },
    {
        'label': _('管理员管理'),
        'app_label': 'user',
        'items': [
            {'name': 'ChfUserProfile', 'label': _('用户'), 'url': '/admin/home/chfuserprofile/', 'url_blank': False},
            {'name': 'auth.group', 'label': _('用户组')},
            # {'name': 'ChfUserProfile', 'permissions': ['core.user']},
        ]
    },
    {
        'label': _('中英文版管理'),
        'app_label': 'version',
        'items': []
    }
]


# 1.0.6之前采用此设置，现已弃用
# JET_SIDE_MENU_CUSTOM_APPS = [
#     # ('home', [
#     #     'SysConfig',
#     #     'ChfAboutResource',
#     #     'ChfAbout',
#     # ]),
#
#     ('home', [
#         '__all__',
#     ]),
#     ('feedback', [
#        'Feedback',
#     ]),
# ]


# JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_INDEX_DASHBOARD = 'chfweb.dashboard.CustomIndexDashboard'
# JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'

# JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(PROJECT_DIR, 'client_secrets.json')
# JET_MODULE_YANDEX_METRIKA_CLIENT_ID = 'YANDEX_METRIKA_CLIENT_ID'
# JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET = 'YANDEX_METRIKA_CLIENT_SECRET'


# 富文本编辑器配置优化
# SUMMERNOTE_CONFIG = {
#     # Using SummernoteWidget - iframe mode
#     'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode
#
#     # Using Summernote Air-mode
#     'airMode': False,
#
#     # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
#     'styleWithSpan': False,
#
#     # Change editor size
#     'width': '80%',
#     'height': '480',
#
#     # Use proper language setting automatically (default)
#     'lang': 'zh-CN',
# }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'fotmat': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'  # 日志格式
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

