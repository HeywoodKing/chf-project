from django.shortcuts import render,redirect, HttpResponse
from django.conf import settings
import logging


# Create your views here.
logger = logging.getLogger("home.views")

def global_setting(req):
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    SITE_AUTHOR = settings.SITE_AUTHOR
    MEDIA_URL = settings.MEDIA_URL

    return locals()

# 首页
def index(req):
    return render(req, 'index.html')


# 关于我们 联系我们
def about(req):
    return render(req, 'about.html')


# 品牌产品
def product_list(req):
    return render(req, 'product_list.html')

# 品牌产品详情
def product_detail(req, id):
    return render(req, 'product_detail.html')

# 品牌合作
def partner(req):
    return render(req, 'partner.html')

# 新闻资讯 社会责任
def news_list(req, mtype):
    if mtype == '0':
        print(mtype)
        chf_title = "新闻资讯"
    else:
        print(mtype)
        chf_title = "社会责任"

    return render(req, 'news_list.html', locals())

# 新闻资讯 社会责任详情
def news_detail(req, mtype, id):
    return render(req, 'news_detail.html')

# 工作机会
def job_list(req):
    return render(req, 'job_list.html')

