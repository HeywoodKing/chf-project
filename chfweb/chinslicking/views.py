from django.shortcuts import render,redirect, HttpResponse
from django import http
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
import logging
import random
import datetime
from home import models


# Create your views here.
logger = logging.getLogger("chinslicking.views")


def global_setting(req):
    SITE_NAME2 = settings.SITE_NAME2
    SITE_DESC2 = settings.SITE_DESC2
    SITE_AUTHOR2 = settings.SITE_AUTHOR2
    MEDIA_URL = settings.MEDIA_URL

    return locals()


# def set_language(req):
#     from django.utils.translation import check_for_language
#     next = req.REQUEST.get('next', None)
#
#     if not next:
#         next = req.META.get('HTTP_REFERER', None)
#     if not next:
#         next = '/'
#
#     response = http.HttpResponseRedirect(next)
#     if req.method == 'POST':
#         lang_code = req.POST.get('language', None)
#
#     if lang_code and check_for_language(lang_code):
#         if hasattr(req, 'session'):
#             req.session['django_language'] = lang_code
#
#         max_age = 60*60*24*365
#         expires = datetime.datetime.strftime(datetime.datetime.utctime() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
#         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code, max_age, expires)
#     return response


# 首页
def index(req):
    index = 0
    return render(req, 'chinslicking/index.html', locals())


# 关于我们 => 品牌介绍
def about(req):
    index = 1
    return render(req, 'chinslicking/about.html', locals())

# 联系我们 为您服务
def contact(req):
    index = 6
    return render(req, 'chinslicking/contact.html', locals())

def layer_coupon_form(req):
    return render(req, 'chinslicking/layer_coupon_form.html')

# 新增抢优惠券的用户信息
def add_coupon(req):
    username = req.POST.get('username', None)
    print(username)
    return HttpResponse('信息保存成功！');


# 品牌产品 => 在线商城
def product_list(req):
    index = 2
    # 获取产品类型
    product_type_list = models.ChfProductType.objects.filter(is_enable=True)
    product_lists = models.ChfProduct.objects.filter(is_enable=True)

    paginator = Paginator(product_lists, 9, 2)  # 每页显示9条，少于2条则合并到上一页
    page = req.GET.get('page')
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)

    # 获取产品
    return render(req, 'chinslicking/product_list.html', locals())


# 品牌产品详情  没有啦
def product_detail(req, id):
    index = 2
    try:
        if id:
            # product = models.ChfProduct.objects.filter(id=id).update(read_count=read_count+1)
            product = models.ChfProduct.objects.get(id=id)

            # 更新浏览量到数据库
            product.read_count += 1
            product.save()

    except Exception as e:
        logger.error(e)

    product_command_list = random.sample(list(models.ChfProduct.objects.filter(is_recommand=True)), 3)

    return render(req, 'chinslicking/product_detail.html', locals())


# 品牌合作 => 合作共赢
def partner(req):
    index = 3
    return render(req, 'chinslicking/partner.html', locals())


# 社会责任 和 新闻资讯合并为一个菜单了
def resp_list(req):
    index = 4

    resp_lists = models.ChfNews.objects.filter(type=1,is_enable=True)
    paginator = Paginator(resp_lists, 10, 2)
    page = req.GET.get('page')
    try:
        resp_list = paginator.page(page)
    except PageNotAnInteger:
        resp_list = paginator.page(1)
    except EmptyPage:
        resp_list = paginator.page(paginator.num_pages)

    resp_lasted = models.ChfNews.objects.filter(type=1)[:10]

    return render(req, 'chinslicking/duty_list.html', locals())


# 社会责任详情
def resp_detail(req, id):
    index = 4
    try:
        if id:
            resp = models.ChfNews.objects.get(id=id)

            resp.read_count += 1
            resp.save()
    except Exception as e:
        logger.error(e)

    resp_lasted = models.ChfNews.objects.filter(type=1)[:10]

    return render(req, 'chinslicking/duty_detail.html', locals())


# 新闻资讯
def news_list(req):
    index = 4

    # 社会责任
    resp_lists = models.ChfNews.objects.filter(type=1, is_enable=True)
    paginator = Paginator(resp_lists, 10, 2)
    page = req.GET.get('page')
    try:
        resp_list = paginator.page(page)
    except PageNotAnInteger:
        resp_list = paginator.page(1)
    except EmptyPage:
        resp_list = paginator.page(paginator.num_pages)

    resp_lasted = models.ChfNews.objects.filter(type=1)[:10]

    # 新闻资讯
    news_lists = models.ChfNews.objects.filter(type=0, is_enable=True)
    paginator = Paginator(news_lists, 10, 2)
    page = req.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    # news_lasted = models.ChfNews.objects.filter(type=0)[:10]

    return render(req, 'chinslicking/news_list.html', locals())


# 新闻资讯
def news_detail(req, id):
    index = 4
    try:
        if id:
            news = models.ChfNews.objects.get(id=id)

            news.read_count += 1
            news.save()
    except Exception as e:
        logger.error(e)

    news_lasted = models.ChfNews.objects.all()[:10]

    return render(req, 'chinslicking/news_detail.html', locals())


# 工作机会
def job_list(req):
    index = 5

    job_list = models.ChfJobRecruit.objects.filter(is_enable=True)

    return render(req, 'chinslicking/job_list.html', locals())

