import os

basedir=os.path.dirname(__file__)
from django.utils.translation import gettext_lazy as _

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
        'slug': 'en-tinywiki-markdown',
        'images': [
            {
                'builtin_id': 1,
                'file': os.path.join(basedir,'Lama.jpg'),
                'alt': "Picture of a lama",
                'description': "A test image",
            },
        ],
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
        'slug': 'de-tinywiki-markdown',
        'images': [
            {
                'builtin_id': 2,
                'file': os.path.join(basedir,'Lama.jpg'),
                'alt': "Bild von einem Lama",
                'description': "Ein Testbild",
            },
        ],
    },    
]
