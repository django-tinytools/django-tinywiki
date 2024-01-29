from markdown.inlinepatterns import InlineProcessor
from xml.etree import ElementTree as etree
from markdown import extensions
from django.shortcuts import reverse
from django.utils.html import escape
import sys

#from .. import settings

class DjangoURLInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        django_url = m.group(2)
        title = m.group(1)

        if not '|' in django_url:
            try:
                url = reverse(django_url)
            except Exception as error:
                print("[tinywiki:django-link] {}!".format(error),file=sys.stderr)
                url = ""
        else:
            urlvec=django_url.split('|')
            try:
                url = reverse(urlvec[0],args=urlvec[1:])
            except Exception as error:
                print("[tinywiki:django-link] {}!".format(error),file=sys.stderr)
                url = ""

        element = etree.Element("a",attrib={'href':url})
        element.text = title

        return element, m.start(0), m.end(0)

class DjangoURLExtension(extensions.Extension):
    def extendMarkdown(self,md):
        LINK_PATTERN="\$\[(.*?)\]\((.+?)\)"
        md.inlinePatterns.register(DjangoURLInlineProcessor(LINK_PATTERN,md),"django_url",175)
