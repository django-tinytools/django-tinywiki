from markdown.inlinepatterns import InlineProcessor
from xml.etree import ElementTree as etree
from markdown import extensions
from django.shortcuts import reverse
from django.utils.html import escape

#from .. import settings

class DjangoURLInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        x = m.group(1).split('|',1)
        django_url_vec = x[0].split(None)
        if len(django_url_vec) == 1:
            try:
                url = reverse(django_url_vec[0])
            except:
                url = ""
        else:
            try:
                url = reverse(django_url_vec[0],args=tuple(django_url_vec[1:]))
            except:
                url = ""

        if len(x) == 1:
            if url:
                title = escape(url)
            else:
                title = "Illegal Link"
        else:
            title = escape(x[1])


        element = etree.Element("a",attrs={'href':url})
        element.text = title

        return element, m.start(0), m.end(0)

class DjangoURLExtension(extensions.Extension):
    def extendMarkdown(self,md):
        LINK_PATTERN="[[url:$(.*?)]]"
        md.inlinePatterns.register(DjangoURLInlineProcessor(LINK_PATTERN,md),"django_url",20)
