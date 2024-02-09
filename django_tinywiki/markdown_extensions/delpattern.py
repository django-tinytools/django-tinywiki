from markdown.inlinepatterns import SimpleTagInlineProcessor
from markdown import extensions


class DelExtension(extensions.Extension):
    def extendMarkdown(self,md):
        LINK_PATTERN=r"()~~(.*?)~~"
        md.inlinePatterns.register(SimpleTagInlineProcessor(LINK_PATTERN,'del'),'del',175)

