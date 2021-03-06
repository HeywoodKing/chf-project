"""chfweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:阿里云 万网
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve
from home import upload
from home import views
from django.views.generic.base import RedirectView
# from jet.dashboard.dashboard_modules import google_analytics_views
# from jet.dashboard.dashboard_modules import yandex_metrika_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/lang/', views.set_lang, name='set_lang'),
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    # url(r'', include('home.urls')),
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),  # 单独上传图片后显示图片的url地址路径
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload.upload_image, name='upload_image'),  # 富文本编辑器上传图片路径
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^i18n/setlang', 'home.views.set_language'),
    # url(r'^setlang/$', 'django.views.i18n.set_language', name = 'setlang'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
]

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    # url(r'^chf/', include('home.urls')),
)

