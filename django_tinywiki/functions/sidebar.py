from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.module_loading import import_string

from .. import settings

def get_left_sidebar_tinywiki_only(request):
    sidebar = [
        {
            'title': _("TinyWiki"),
            'items': [
                {
                    'title': _('Main Page'),
                    'page': _("en-tinywiki-index"),
                },
                {
                    'title': _("Page overview"),
                    'url': settings.TINYWIKI_PAGE_OVERVIEW_URL,
                },
                {
                    'title': _("Markdown"),
                    'page': _("en-tinywiki-markdown"),
                },
                {
                    'title': _("Configuration"),
                    'page': _("en-tinywiki-settings"),
                }
            ]
        },
    ]

    return sidebar

def get_left_sidebar(request):
    sidebar = get_left_sidebar_tinywiki_only(request)
    if settings.TINYWIKI_LEFT_SIDEBAR:
        sidebar += settings.TINYWIKI_LEFT_SIDEBAR
    if isinstance(settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION,str):
        func = import_string(settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION)
        if callable(func):
            sidebar += func(request)
    elif callable(settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION):
        sidebar += settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION(request)

    return sidebar
