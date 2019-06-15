from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import http
from django.utils.translation import ugettext as _
from django.utils.timezone import now, timedelta
from datetime import datetime
import logging
import random
import json
import socket
import pytz
from home import models


# Create your views here.
logger = logging.getLogger("me")


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
#         expires = datetime.datetime.strftime(datetime.datetime.utctime() +
#         datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
#         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code, max_age, expires)
#     return response


# 首页
def index(req):
    index = 0
    water_qty_model = models.ChfWateringQty.objects.all()
    if water_qty_model:
        water_qty = water_qty_model[0]
    else:
        water_qty = models.ChfWateringQty()

    index_plate_list = models.ChfIndexPlate.objects.filter(is_enable=True)

    return render(req, 'home/index.html', locals())


# 关于我们 => 品牌介绍
def about(req):
    index = 1

    try:
        comp_about_model = models.ChfAbout.objects.get(is_enable=True)
    except Exception as e:
        comp_about_model = models.ChfAbout()
        logger.error(e)
    # 反向查找
    culture = comp_about_model.about_resource.filter(type_code=1)
    honor = comp_about_model.about_resource.filter(type_code=2)
    aptitude = comp_about_model.about_resource.filter(type_code=3)
    # comp_about = {
    #     'comp': comp_about_model,
    #     'culture': culture,
    #     'honor': honor,
    #     'aptitude': aptitude
    # }

    comp_history_list = models.ChfCompanyHistory.objects.filter(is_enable=True)

    return render(req, 'home/about.html', locals())


# 联系我们 为您服务
def contact(req):
    index = 6
    return render(req, 'home/contact.html', locals())


def layer_coupon_form(req):
    return render(req, 'home/layer_coupon_form.html')


# 新增抢优惠券的用户信息
def add_coupon(req):
    res = {
        'code': -1,
        'flag': 'fail',
        'msg': '异常错误！',
        'data': None
    }

    if req.method == 'POST':
        # 接收参数
        # csrf_token=afdasfasf&username=aaa&phone=13256235689&email=aaa@123.com&sex=adfsfd
        # json_params = req.body.replace('=', '":"').replace('&', '","')
        # print(json_params)
        username = req.POST.get('username', None)
        phone = req.POST.get('phone', None)
        email = req.POST.get('email', None)
        sex = req.POST.get('sex', None)
        birthday = req.POST.get('birthday', datetime.now().replace(tzinfo=pytz.utc).strftime("%Y-%m-%d"))

        # 保存记录
        model = models.ChfApplyRecord(name=username, phone=phone, email=email, sex=sex, birthday=birthday)
        model.save()

        # models.ChfApplyRecord.objects.create(name=username, phone=phone, email=email, sex=sex)

        # 返回结果
        res['code'] = 0
        res['flag'] = 'success'
        res['msg'] = '保存成功'
        res['data'] = None

    return HttpResponse(json.dumps(res), content_type='application/json')


def get_host_ip():
    """
    查询本机ip
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


# 增加浇水水量
def add_watering_qty(req):
    res = {
        'code': -1,
        'flag': 'fail',
        'msg': '异常错误！',
        'data': None
    }

    if req.method == 'POST':
        # 接收参数
        # 获取客户端IP地址，判断同一个IP一天不能浇水超过3次
        client_ip = req.META['REMOTE_ADDR'].split(':')[0]
        remote_host = req.META['REMOTE_HOST']
        client_host = remote_host if remote_host else req.META['USERDOMAIN']
        client_user_agent = req.META['HTTP_USER_AGENT']
        server_ip = get_host_ip()
        server_host = req.META['SERVER_NAME']
        server_port = req.META['SERVER_PORT']
        # print(req.META)
        # 获取当天的日期,日期格式为yyyy-MM-dd
        # curr_date = now().date() + timedelta(days=0)
        # 获取当前时间
        curr_now = datetime.now()  # .replace(pytz.utc)
        print(curr_now)
        # 获取今天零点
        start_date = curr_now - timedelta(hours=curr_now.hour,
                                          minutes=curr_now.minute,
                                          seconds=curr_now.second,
                                          microseconds=curr_now.microsecond)
        # 获取今天23:59:59
        end_date = start_date + timedelta(hours=23, minutes=59, seconds=59)
        # 获取昨天的当前时间
        # yesterday_now = curr_now - timedelta(hours=23, minutes=59, seconds=59)
        # 获取明天的当前时间
        # tomorrow_now = curr_now + timedelta(hours=23, minutes=59, seconds=59)

        # start_date = datetime.date(2019, 5, 1)
        # end_date = datetime.date(2019, 6, 1)

        ip_count = models.ChfUserWateringRecord.objects\
            .filter(client_ip=client_ip, create_time__range=(start_date, curr_now))\
            .count()
        if ip_count > 3:
            # 返回结果
            res['code'] = 1
            res['flag'] = 'fail'
            res['msg'] = '浇水失败，您今天浇水次数太多了，<br>明天再继续吧！'
            res['data'] = None
            return HttpResponse(json.dumps(res), content_type='application/json')

        # amount_str = req.POST.get('amount', 0)
        # amount = int(amount_str)

        amount = random.randint(1, 20)

        # 保存本次浇水水量到余额表
        water_qty = models.ChfWateringQty.objects.all()[0]

        # 保存本次用户浇水记录
        end_amount = water_qty.amount + amount
        user_watering_record = models.ChfUserWateringRecord(
            client_ip=client_ip,
            client_host=client_host,
            client_user_agent=client_user_agent,
            server_ip=server_ip,
            server_host=server_host,
            server_port=server_port,
            init_amount=water_qty.amount,
            amount=amount,
            final_amount=end_amount)
        user_watering_record.save()

        water_qty.amount = end_amount
        water_qty.total_amount = water_qty.total_amount + amount
        water_qty.save()

        # 返回结果
        res['code'] = 0
        res['flag'] = 'success'
        res['msg'] = '浇水成功'
        res['data'] = end_amount
    else:
        res['code'] = 2
        res['flag'] = 'fail'
        res['msg'] = '非法请求'
        res['data'] = None

    return HttpResponse(json.dumps(res), content_type='application/json')


# 品牌产品 => 在线商城
def product_list(req):
    index = 2
    # 获取产品类型
    product_type_list = models.ChfProductType.objects.filter(is_enable=True)
    product_lists = models.ChfProduct.objects.filter(is_enable=True)

    paginator = Paginator(product_lists, 6)  # 每页显示6条，第三个参数2: 少于2条则合并到上一页
    page = req.GET.get('page')
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)

    # 获取产品
    return render(req, 'home/product_list.html', locals())


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

    return render(req, 'home/product_detail.html', locals())


# 品牌合作 => 合作共赢
def partner(req):
    index = 3
    try:
        policy = models.ChfCooperationPolicy.objects.get(is_enable=True)
    except Exception as e:
        policy = None
        logger.error(e)

    try:
        superiority = models.ChfCooperationSuperiority.objects.get(is_enable=True)
    except Exception as e:
        superiority = None
        logger.error(e)

    try:
        question = models.ChfCooperationQuestion.objects.get(is_enable=True)
    except Exception as e:
        question = None
        logger.error(e)

    return render(req, 'home/partner.html', locals())


# 社会责任 和 新闻资讯合并为一个菜单了
def resp_list(req):
    index = 4

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

    return render(req, 'home/duty_list.html', locals())


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

    return render(req, 'home/duty_detail.html', locals())


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
        logger.error('传入的页码错误')
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
        logger.error('空页')

    # news_lasted = models.ChfNews.objects.filter(type=0)[:10]

    return render(req, 'home/news_list.html', locals())


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

    return render(req, 'home/news_detail.html', locals())


# 工作机会
def job_list(req):
    index = 5

    job_list = models.ChfJobRecruit.objects.filter(is_enable=True)

    return render(req, 'home/job_list.html', locals())

