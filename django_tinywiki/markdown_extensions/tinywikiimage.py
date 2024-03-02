from collections.abc import Iterable, Mapping
from re import Match
from typing import Any
from xml.etree.ElementTree import Element
from django.utils.translation import gettext as _
from markdown.core import Markdown
from markdown.inlinepatterns import InlineProcessor
from markdown import extensions
from xml.etree import ElementTree as etree
from django.urls import reverse
from ..models.wiki import WikiImage,WikiPage

class ImageInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match, data):
        image_alt = m.group(1)
        image_desc = m.group(1)
        image_url = m.group(2)

        element = etree.Element("div",attrib={'class':"wiki-image"})
        element.append(etree.Element("img",attrib={"alt":image_alt,"src":image_url}))
        element.append(etree.Element("br"))
        desc_element = etree.Element("span")
        desc_element.text = image_desc
        element.append(desc_element)

        return element, m.start(0), m.end(0)

class ImageDescriptionInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match, data):
        image_alt = m.group(1)
        image_desc = m.group(2)
        image_url = m.group(3)

        element = etree.Element("div",attrib={'class':"wiki-image"})
        element.append(etree.Element("img",attrib={"alt":image_alt,"src":image_url}))
        element.append(etree.Element("br"))
        desc_element = etree.Element("span")
        desc_element.text = image_desc
        element.append(desc_element)

        return element, m.start(0), m.end(0)

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
            link_element = etree.Element("a",attrib={'href':img.image.url})
            link_element.append(etree.Element("img", attrib=attrib))
            if img.description:
                link_element.append(etree.Element("br"))
                desc_element = etree.Element("span",attrib={'class':'wiki-image-description'})
                desc_element.text = img.description
                link_element.append(desc_element)
            element.append(link_element)

            
        except WikiImage.DoesNotExist:
            element = etree.Element("div", attrib={"class":"wiki-image image-not-found"})
            element.text = _("Image with id {img_id} not found!".format(img_id=m.group(1)))
        
        return element, m.start(0), m.end(0)

class TinywikiBuiltinImageInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match, data):
        builtin_id = int(m.group(1))

        try:
            img = WikiImage.objects.get(builtin_id=builtin_id)

            element = etree.Element("div",attrib={'class':'wiki-image'})
            link_element = etree.Element("a",attrib={'href':img.image.url})
            link_element.append(etree.Element("img",attrib={'alt':img.alt,'src':img.image_wiki.url}))
            link_element.append(etree.Element("br"))
            desc_element = etree.Element("span")
            desc_element.text = img.description
            link_element.append(desc_element)
            element.append(link_element)
            

        except WikiImage.DoesNotExist:
            element = etree.Element("div",attrib={'class':'wiki-image image-not-found'})
            element.text = _("Image with builtin id {img_id} not found!".format(img_id=builtin_id))

        return element, m.start(0), m.end(0)
class TinywikiLinkedImagesInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        if not hasattr(self,'wiki_page') or not self.wiki_page:
            element = etree.Element("span",attrib={'class':'error'})
            element.text = _("Can not find linked images for unknown wiki-page!")
            return element, m.start(0), m.end(0)
        
        edit_page = getattr(self,'edit_page',False)
            
        try:
            page = WikiPage.objects.get(slug=self.wiki_page)
        except WikiPage.DoesNotExist:
            element = etree.Element("span",attrib={'class':'error'})
            element.text = _("Can not find wiki-page {page_id}!").format(page_id=self.wiki_page)
            return element, m.start(0), m.end(0)

        element = etree.Element("div", attrib={'class':'wiki-linked-images'})
        if edit_page:
            ctrl_element = etree.Element("div",attrib={'class':'wiki-linked-images-control'})
            add_image_element = etree.Element("a",attrib={'href':reverse('tinywiki:image-upload',kwargs={'page':self.wiki_page})})
            add_image_element.text = _("Upload Image")
            ctrl_element.append(add_image_element)
            element.append(ctrl_element)

        grid_element = etree.Element("div", attrib={'class':"wiki-linked-image-grid"})

        for wi in page.images.all().order_by('id'):
            img_div_element = etree.Element("div",attrib={'class':"wiki-linked-image-grid-item"})
            img_link_element = etree.Element("a",attrib={'href':wi.image.url})
            img_link_element.append(etree.Element('img',attrib={'class':'wiki-linked-image-grid-item-image',
                                                               'alt':wi.alt,
                                                               'src':wi.image_preview.url}))
            img_text_element = etree.Element("div",attrib={'class':'wiki-linked-image-grid-item-text'})
            if wi.description:
                img_text = wi.description
            else:
                img_text = wi.alt
            img_text_element.text = "#{img_id} - {img_text}".format(img_id=wi.id,img_text=img_text)
            img_link_element.append(img_text_element)
            img_div_element.append(img_link_element)
            grid_element.append(img_div_element)


        element.append(grid_element)

        return element, m.start(0), m.end(0)

class TinywikiImageExtension(extensions.Extension):
    def extendMarkdown(self, md: Markdown):
        LINK_PATTERN_TW = "\!\[\[([0-9]+?)\]\]"
        LINK_PATTERN_TW_BUILTIN = "\!\[\[\!([\-]?[0-9]+?)\]\]"
        LINK_PATTER_DESC_URL = "\!\[(.*?)\]\[(.*?)\]\((.+?)\)"
        LINK_PATTERN_URL = "\!\[(.*?)\]\((.+?)\)"
        md.inlinePatterns.register(TinywikiImageInlineProcessor(LINK_PATTERN_TW,md),"tinywiki-image",180)
        md.inlinePatterns.register(TinywikiBuiltinImageInlineProcessor(LINK_PATTERN_TW_BUILTIN,md),"tinywiki-builtin-image",180)
        md.inlinePatterns.register(ImageDescriptionInlineProcessor(LINK_PATTER_DESC_URL,md),"image-desc",180)
        md.inlinePatterns.register(ImageInlineProcessor(LINK_PATTERN_URL,md),'image',175)

class TinywikiLinkedImagesExtension(extensions.Extension):
    def __init__(self,wiki_page=None,edit_page=False,**kwargs: Any) -> None:
        self.config = {
            'wiki_page': [wiki_page, 'Slug for TinyWiki page'],
            'edit_page': [edit_page, 'User can edit page'],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md: Markdown):
        LINK_PATTERN = "\[WIKI\-IMAGES\]"
        processor = TinywikiLinkedImagesInlineProcessor(LINK_PATTERN,md)
        processor.wiki_page = self.getConfig('wiki_page')
        processor.edit_page = self.getConfig('edit_page')
        md.inlinePatterns.register(processor,"tinywiki-linked-image",75)

    def setConfig(self, key: str, value: Any) -> None:
        return super().setConfig(key, value)
    
    def setConfigs(self, items: Mapping[str, Any] | Iterable[tuple[str, Any]]) -> None:
        return super().setConfigs(items)
