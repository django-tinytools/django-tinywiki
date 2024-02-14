from markdown.inlinepatterns import InlineProcessor
from markdown import extensions
from xml.etree import ElementTree as etree

from django.shortcuts import reverse
from django.utils.html import escape

from .. import settings
from .. import models


class TinywikiLinkInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        slug = m.group(1)
    
        try:
            page = models.WikiPage.objects.get(slug=slug)
            title = escape(page.title)
        except models.WikiPage.DoesNotExist:
            title = slug
    
        url = str(reverse(settings.TINYWIKI_PAGE_VIEW_URL_TEMPLATE,args=[slug]))
                
        element = etree.Element("a",attrib={'href':url})
        element.text = title

        
        return element, m.start(0), m.end(0)

class TinyWikiLinkTitleInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        slug = m.group(2)
        title = m.group(1)
    
        url = str(reverse(settings.TINYWIKI_PAGE_VIEW_URL_TEMPLATE,args=[slug]))

        element = etree.Element("a",attrib={'href':url})
        element.text = title

        return element, m.start(0), m.end(0)
class TinywikiLinkExtension(extensions.Extension):
    def extendMarkdown(self,md):
        LINK_PATTERN0 = "\[\[(.*?)\]\]\((.+?)\)"
        LINK_PATTERN1 = "\[\[(.+?)\]\]"
        md.inlinePatterns.register(TinyWikiLinkTitleInlineProcessor(LINK_PATTERN0,md),"tinywiki_linktitle",175)
        md.inlinePatterns.register(TinywikiLinkInlineProcessor(LINK_PATTERN1,md),"tinywiki_link",170)

        
