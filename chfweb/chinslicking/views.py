from django.shortcuts import render,redirect, HttpResponse
from django.conf import settings
import logging


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
    return render(req, 'chinslicking/product_list.html', locals())

# 品牌产品详情
def product_detail(req, id):
    return render(req, 'chinslicking/product_detail.html')

# 品牌合作
def partner(req):
    index = 3
    return render(req, 'chinslicking/partner.html', locals())

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

    return render(req, 'chinslicking/news_list.html', locals())

# 新闻资讯
def news_detail(req, id):
    return render(req, 'chinslicking/news_detail.html', locals())


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

    return render(req, 'chinslicking/duty_list.html', locals())

# 社会责任详情
def resp_detail(req, id):
    return render(req, 'chinslicking/duty_detail.html', locals())


# 工作机会
def job_list(req):
    index = 6
    return render(req, 'chinslicking/job_list.html', locals())

