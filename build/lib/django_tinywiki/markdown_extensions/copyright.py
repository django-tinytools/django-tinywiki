from re import Match
from markdown.inlinepatterns import InlineProcessor
from markdown import extensions
from xml.etree.ElementTree import Element

class CopyrightInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match[str], data):
        element = Element("span")
        element.text = "&copy;"
        return element,m.start(0),m.end(0)
    
class RegisteredInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match[str], data):
        element = Element("span")
        element.text = "&reg;"
        return element,m.start(0),m.end(0)

class TrademarkInlineProcessor(InlineProcessor):
    def handleMatch(self, m: Match[str], data):
        element = Element("span")
        element.text = "&trade;"
        return element,m.start(0),m.end(0)


class CopyrightExtension(extensions.Extension):
    def extendMarkdown(self,md):
        LINK_PATTERN_COPY=r"\(C\)"
        LINK_PATTERN_REG=r"\(R\)"
        LINK_PATTERN_TM=r"\(TM\)"
        md.inlinePatterns.register(CopyrightInlineProcessor(LINK_PATTERN_COPY,md),'copyright',70)
        md.inlinePatterns.register(RegisteredInlineProcessor(LINK_PATTERN_REG,md),'registered',75)
        md.inlinePatterns.register(TrademarkInlineProcessor(LINK_PATTERN_TM,md),'trademark',75)

