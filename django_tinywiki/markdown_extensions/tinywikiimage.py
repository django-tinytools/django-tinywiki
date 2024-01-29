from re import Match
from xml.etree.ElementTree import Element
from markdown.core import Markdown
from markdown.inlinepatterns import InlineProcessor
from markdown import extensions
from xml.etree import ElementTree as etree

from ..models.wiki import WikiImage,WikiPage

class TinywikiImageInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match[str], data):
        try:
            img_id = int(m.group(0))
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
                desc = etree.Element("span",attrib={'class':'wiki-image-description'})
                desc.text = img.description
                element.append(desc)

        except Exception as error:
            element = etree.Element("span")
            element.text = m.string
        
        return element, m.start(0), m.end(0)

class TinywikiImageExtension(extensions.Extension):
    def extendMarkdown(self, md: Markdown):
        LINK_PATTERN = "\!\[\[\([0-9]+?)]\]"
        md.inlinePatterns.register(TinywikiImageInlineProcessor(LINK_PATTERN,md),"tinywiki-image",255)
