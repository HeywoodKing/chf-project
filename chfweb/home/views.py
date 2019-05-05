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
    index = 0
    return render(req, 'index.html', locals())


# 关于我们 联系我们
def about(req):
    index = 1
    return render(req, 'about.html', locals())

def contact(req):
    index = 7
    return render(req, 'contact.html', locals())


# 品牌产品
def product_list(req):
    index = 2
    return render(req, 'product_list.html', locals())

# 品牌产品详情
def product_detail(req, id):
    return render(req, 'product_detail.html')

# 品牌合作
def partner(req):
    index = 3
    return render(req, 'partner.html', locals())

# 新闻资讯
def news_list(req):
    # if mtype == '0':
    #     print(mtype)
    #     chf_title = "新闻资讯"
    #     index = 5
    # else:
    #     print(mtype)
    #     chf_title = "社会责任"
    #     index = 4
    index = 5

    return render(req, 'news_list.html', locals())

# 新闻资讯
def news_detail(req, id):
    return render(req, 'news_detail.html', locals())


# 社会责任
def resp_list(req):
    # if mtype == '0':
    #     print(mtype)
    #     chf_title = "新闻资讯"
    #     index = 5
    # else:
    #     print(mtype)
    #     chf_title = "社会责任"
    #     index = 4
    index = 4

    return render(req, 'duty_list.html', locals())

# 社会责任详情
def resp_detail(req, id):
    return render(req, 'duty_detail.html', locals())


# 工作机会
def job_list(req):
    index = 6
    return render(req, 'job_list.html', locals())

