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
        'file': os.path.join(basedir,'de.index.md'),
        'language': 'de',
        'title': "TinyWiki Hauptseite",
        'slug': 'de-tinywiki-index',
    },
]
