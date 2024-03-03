from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.module_loading import import_string
from django.utils.html import escape
from ..models.wiki import WikiPage

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

def get_left_sidebar_data(request):
    
    sidebar = []
    if settings.TINYWIKI_LEFT_SIDEBAR_DATA:
        sidebar += settings.TINYWIKI_LEFT_SIDEBAR_DATA
    if isinstance(settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION,str):
        func = import_string(settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION)
        if callable(func):
            sidebar += func(request)
    elif callable(settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION):
        sidebar += settings.TINYWIKI_LEFT_SIDEBAR_FUNCTION(request)

    if settings.TINYWIKI_SHOW_TINYWIKI_LEFT_SIDEBAR_ITEMS:
        sidebar += get_left_sidebar_tinywiki_only(request)

    return sidebar

def render_left_sidebar(request,*args,**kwargs):
    sidebar_sections = []

    for sect_spec in get_left_sidebar_data(request):
        sect = "<div class=\"left-sidebar-section\">\n"
        sect += ("\t<div class=\"left-sidebar-section-title\">" + escape(sect_spec['title']) + "</div>\n")
        for item_spec in sect_spec['items']:
            link_number = 1
            if 'widget' in item_spec:
                sect += ("\t\t" + sect['widget'])
            elif 'page' in item_spec:
                if 'title' in item_spec:
                    title = item_spec['title']
                else:
                    try:
                        wikipage = WikiPage.objects.get(slug=item_spec['page'])
                        title = wikipage.title
                    except:
                        title = item_spec['page']

                sect += ("\t\t<div class=\"left-sidebar-item\"><a href=\""
                         + reverse(settings.TINYWIKI_PAGE_VIEW_URL_TEMPLATE,kwargs={'page':item_spec['page']}) 
                         + "\">" + escape(item_spec['title']) + "</a></div>\n")
                
            elif 'url' in item_spec:
                if 'title' in item_spec:
                    title = item_spec['title']
                else:
                    title = _("Link #{number}").format(number=link_number)
                    link_number += 1
                
                sect += ("\t\t<div class=\"left-sidebar-item\"><a href=\"" + item_spec['url'] + "\">" 
                         + title + "</a></div>\n")
        sect += "\t</div>\n<div>"
        sidebar_sections.append(sect)

    if sidebar_sections:
        ret =  "\n".join(sidebar_sections)
        return ret
    return ""

def render_right_sidebar(request,*args,page=None,**kwargs):
    wikipage = None
    if page is not None:
        if isinstance(page,str):
            try:
                wikipage = WikiPage.objects.get(slug="page")
            except:
                pass
        elif isinstance(page,int):
            try:
                wikipage = WikiPage.objects.get(id=page)
            except:
                pass
        else:
            wikipage = page

    ret=""

    if wikipage:
        for wi in wikipage.images.filter(image_preview__isnull=False):
            if wi.description:
                desc = wi.description
            else:
                desc = wi.alt
                
            ret += ("<div class=\"right-sidebar-item\">"
                     + "<a class=\"right-sidebar-image-link\" href=\"{original_image_url}\">"
                     + "<img class=\"right-sidebar-image\" src=\"{preview_image_url}\" /><br>"
                     + "{description}</a></div>").format(
                         original_image_url=wi.image.url,
                         preview_image_url=wi.image_preview.url,
                         description=escape(desc))
    return ret
