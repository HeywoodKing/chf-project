from django.shortcuts import render,redirect, HttpResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
import logging
import random
from home import models


# Create your views here.
logger = logging.getLogger("chinslicking.views")

def global_setting(req):
    SITE_NAME2 = settings.SITE_NAME2
    SITE_DESC2 = settings.SITE_DESC2
    SITE_AUTHOR2 = settings.SITE_AUTHOR2
    MEDIA_URL = settings.MEDIA_URL

    return locals()

# 首页
def index(req):
    index = 0
    return render(req, 'chinslicking/index.html', locals())


# 关于我们 联系我们
def about(req):
    index = 1
    return render(req, 'chinslicking/about.html', locals())

def contact(req):
    index = 7
    return render(req, 'chinslicking/contact.html', locals())




# 品牌产品
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

# 品牌产品详情
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

# 品牌合作
def partner(req):
    index = 3
    return render(req, 'chinslicking/partner.html', locals())


# 社会责任
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
    index = 5

    news_lists = models.ChfNews.objects.filter(type=0,is_enable=True)
    paginator = Paginator(news_lists, 10, 2)
    page = req.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    news_lasted = models.ChfNews.objects.filter(type=0)[:10]

    return render(req, 'chinslicking/news_list.html', locals())

# 新闻资讯
def news_detail(req, id):
    index = 5
    try:
        if id:
            news = models.ChfNews.objects.get(id=id)

            news.read_count += 1
            news.save()
    except Exception as e:
        logger.error(e)

    news_lasted = models.ChfNews.objects.filter(type=0)[:10]

    return render(req, 'chinslicking/news_detail.html', locals())


# 工作机会
def job_list(req):
    index = 6

    job_list = models.ChfJobRecruit.objects.filter(is_enable=True)

    return render(req, 'chinslicking/job_list.html', locals())

