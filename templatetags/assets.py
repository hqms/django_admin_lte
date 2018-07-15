# coding=utf-8

from django import template
from django.utils.safestring import mark_safe

from django_admin_lte.Assets import Assets, Menu
from django_admin_lte.apps import DjangoAdminLteConfig

register = template.Library()


@register.simple_tag(takes_context=True)
def css(context, *args, **kwargs):
    """

    :param context:
    :return:
    """
    css = Assets('css')

    if not args:
        css.css = DjangoAdminLteConfig.default_css
    else:
        css.css = args

    return mark_safe(css.render())


@register.simple_tag(takes_context=True)
def js(context, *args, **kwargs):
    """

    :param context:
    :return:
    """
    css = Assets('js')

    if not args:
        css.js = DjangoAdminLteConfig.default_js
    else:
        css.js = args

    return mark_safe(css.render())


@register.simple_tag(takes_context=True)
def menu(context, *args, **kwargs):

    menu = Menu()
    menu.add('main_navigation', {
                                    'label': 'Main Navigation',
                                    'items': [
                                        {
                                            'label': 'Dashboard',
                                            'is_active': True,
                                            'class': 'fa fa-dashboard',
                                            'items': [
                                                {
                                                    'label': 'Dashboard v1',
                                                    'is_active': True,
                                                    'url': './html',
                                                    'class': 'fa fa-circle-o'
                                                }
                                            ]
                                        }
                                    ]
                                })

    return mark_safe(menu.render())
