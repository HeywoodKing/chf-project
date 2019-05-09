# !-*- coding: utf-8 -*-
# @Author  : ching(opencoding@hotmail.com)
# @Date    : 2019/05/02
# @Link    : www.cnblogs.com/ching126/ or blog.csdn.net/chenhongwu666
# @Version :
# @Desc    :

from django import template
from django.utils.html import format_html


register = template.Library()

@register.filter
def my_upper(val):
    print('val from template:', val)
    return val.upper()


@register.simple_tag
def circle_page(curr_page, loop_page):
    offset = abs(curr_page - loop_page)

    if offset < 3:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href="?page=%s">%s</a></li>' % (loop_page, loop_page)
        else:
            page_ele = '<li><a href="?page=%s">%s</a></li>' % (loop_page, loop_page)

        return format_html(page_ele)

    else:
        return ''

@register.filter(name='displayName')
def displayName(value, arg):
    return eval('value.get_' + arg + '_display()')