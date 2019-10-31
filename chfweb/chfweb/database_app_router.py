# !-*- coding: utf-8 -*-
# @Author  : ching(flackmaster@163.com)
# @Date    : 2019/02/25
# @Link    : http://www.cnblogs.com/ching126/
# @Version : $
# @Desc    :

from django.conf import settings


class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        app_label = model._mata.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            return settings.DATABASES_APPS_MAPPING[app_label]
        return None

    def db_for_writer(self, model, **hints):
        app_label = model._mata.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            return settings.DATABASES_APPS_MAPPING[app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = settings.DATABASES_APPS_MAPPING.get(obj1._mata.app_label)
        db_obj2 = settings.DATABASES_APPS_MAPPING.get(obj2._mata.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False

    def db_for_migrate(self, db, app_label, model_name=None, **hints):
        if db in settings.DATABASES_APPS_MAPPING.values():
            return settings.DATABASES_APPS_MAPPING.get(app_label) == db
        elif app_label in settings.DATABASES_APPS_MAPPING:
            return False
        return None



