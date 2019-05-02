# !-*- coding: utf-8 -*-
# @Author  : ching(opencoding@hotmail.com)
# @Date    : 2019/05/02
# @Link    : www.cnblogs.com/ching126/ or blog.csdn.net/chenhongwu666
# @Version : 
# @Desc    :

from django.urls import path
from django.conf.urls import url
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product_list/', views.product_list, name='product_list'),
    url(r'^product_detail/(?P<id>)\d+/$', views.product_detail, name='product_detail'),
    path('news_list/', views.news_list, name='news_list'),
    url(r'^news_detail/(?P<id>)\d+/$', views.news_detail, name='news_detail'),
    path('partner/', views.partner, name='partner'),
    path('job_list/', views.job_list, name='job_list'),
]
