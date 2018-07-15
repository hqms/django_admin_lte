# coding=utf-8
from sqlparse.keywords import is_keyword


class Assets:
    """
    thanks to https://github.com/dnaextrim/django_adminlte_x/blob/master/adminlte/Assets.py
    """
    css = {}
    js = {}
    type = ''

    def __init__(self, type):
        self.type = type

    def render(self):

        """
        @TODO src for non static or from http url

        :return:
        """

        ret = ''

        if self.type.lower() == 'css':
            if not isinstance(self.css, dict):

                for r in self.css:
                    ret += '<link rel="stylesheet" type="text/css" href="/static/%s" />\n' % r
            else:
                for rel in self.css:
                    for r in self.css[rel]:
                        ret += '<link rel="%s" type="text/css" href="/static/%s" />\n' % (rel, r)

        elif self.type.lower() == 'js':

            for r in self.js:
                ret += '<script type="text/javascript" src="/static/%s"></script>\n' % (r)

        return ret


class Menu:
    """
    :class Menu
    """
    menu_group = {}

    def add(self, key, menu_item=()):
        """
        add menu item
        """

        self.menu_group[key] = menu_item

    def render(self):
        """
        @TODO recursively generated

        :return:
        """
        result = ''
        for key, menu in self.menu_group.items():
            cls = ''

            result += '<li class="header">%s</li>' % (menu['label'])

            if 'items' in menu and menu['items']:

                cls = ''
                if 'is_active' in menu and menu['is_active']:
                    cls = 'active'

                treeview = ''
                if menu['items']:
                    treeview = 'treeview'


                result += '<li class="%s %s">' % (cls, treeview)
                for item in menu['items']:
                    active = ''
                    if 'is_active' in item and item['is_active']:
                        active = 'active'

                    cls = ''
                    if 'class' in item and item['class']:
                        cls = item['class']

                    additional = ''
                    if 'items' in item and item['items']:
                        additional = '<span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span>'

                    result += '<a href="#">' \
                              ' <i class="%s"></i> ' \
                              '     <span>%s</span>' \
                              '     %s' \
                              '</a>' % (cls, item['label'], additional)

                    if 'items' in item and item['items']:
                        for i in item['items']:
                            result += ''

                result += '</li>'

        return result


def css(assets):
    """
    render CSS assets

    :param assets:
    """
    Assets.css = assets


def js(assets):
    """
    Render JS assets
    :param assets:
    """
    Assets.js = assets
