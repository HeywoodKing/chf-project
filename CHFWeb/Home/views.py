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

def index(req):
    return render(req, 'index.html')