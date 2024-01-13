from markdown.inlinepatterns import InlineProcessor
from xml.etree import ElementTree as etree
from markdown import extensions
from django.shortcuts import reverse
from django.utils.html import escape

from .. import settings
from .. import models

class TinywikiLinkInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        x = m.group(1).split(None,1)
        if len(x) == 1:
            slug = x[0]
            title = None
        else:
            slug = x[0]
            title = escape(x[1])

        url=reverse(settings.TINYWIKI_PAGE_VIEW_URL,slug)

        if title is None:
            try:
                page = models.WikiPage.objects.get(slug=slug)
                title = escape(page.title)
            except models.WikiPage.DoesNotExist:
                title = slug

        element = etree.Element("a",attrs={'href':url})
        element.text = title

        return element, m.start(0), m.end(0)

class TinywikiLinkExtension(extensions.Extension):
    def extendMarkdown(self,md):
        LINK_PATTERN="[[wiki:$(.*?)]]"
        md.inlinePatterns.register(TinywikiLinkInlineProcessor(LINK_PATTERN,md),"tinywiki_link",20)
