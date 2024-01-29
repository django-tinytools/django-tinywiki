import os

basedir=os.path.dirname(__file__)

BUILTIN_PAGES = [
    {
        'file': os.path.join(basedir,'en.index.md'),
        'language': 'en',
        'title': "TinyWiki Index",
        'slug': 'en-tinywiki-index',
    },
    {
        'file': os.path.join(basedir,'en.markdown.md'),
        'language': 'en',
        'title': "Markdown",
        'slug': 'en-tinywiki-markdown'
    },
    {
        'file': os.path.join(basedir,'de.index.md'),
        'language': 'de',
        'title': "TinyWiki Hauptseite",
        'slug': 'de-tinywiki-index',
    },
    {
        'file': os.path.join(basedir,'de.markdown.md'),
        'language': 'de',
        'title': "Markdown",
        'slug': 'de-tinywiki-markdown'
    },    
]
