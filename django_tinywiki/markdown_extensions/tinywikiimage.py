from re import Match
from xml.etree.ElementTree import Element
from django.utils.translation import gettext as _
from markdown.core import Markdown
from markdown.inlinepatterns import InlineProcessor
from markdown import extensions
from xml.etree import ElementTree as etree

from ..models.wiki import WikiImage,WikiPage

class TinywikiImageInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match[str], data):
        try:
            img_id = int(m.group(1))
            img = WikiImage.objects.get(id=img_id)

            if img.image_wiki:
                attrib = {'src':img.image_wiki.url}
            else:
                attrib = {'src':img.image.url}

            if img.alt:
                attrib['alt'] = img.alt

            
            element = etree.Element("div",attrib={'class':'wiki-image'})
            element.append(etree.Element("img", attrib=attrib))
            if img.description:
                element.append(etree.Element("br"))
                desc = etree.Element("span",attrib={'class':'wiki-image-description'})
                desc.text = img.description
                element.append(desc)

            
        except Exception as error:
            element = etree.Element("div", attrib={"class":"wiki-image image-not-found"})
            element.text = _("Image with id {img_id} not found!".format(img_id=m.group(1)))
        
        return element, m.start(0), m.end(0)

class TinywikiImageExtension(extensions.Extension):
    def extendMarkdown(self, md: Markdown):
        LINK_PATTERN = "\!\[\[([0-9]+?)\]\]"
        md.inlinePatterns.register(TinywikiImageInlineProcessor(LINK_PATTERN,md),"tinywiki-image",300)
