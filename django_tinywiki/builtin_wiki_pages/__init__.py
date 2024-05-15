# -*- coding: UTF-8 -*-
import os

basedir=os.path.dirname(__file__)
from django.utils.translation import gettext_lazy as _

# BUILTIN_PAGES.images.builtin_ids:
#   en -1       to      -999
#   de -1000    to      -1999

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
                'builtin_id': -1,
                'file': os.path.join(basedir,'Lama.jpg'),
                'alt': "Picture of a lama",
                'description': "A test image",
                'sidebar': True,
            },
            {
                'builtin_id': -2,
                'file': os.path.join(basedir,'vineyard-styria.jpg'),
                'alt': "Vineyard in Styria",
                'description': "A vineyard in Styria (Austria)",
                'sidebar': True,
            }
        ],
    },
    {
        'file': os.path.join(basedir,'en.settings.md'),
        'language':'en',
        'title': 'TinyWiki Settings',
        'slug': 'en-tinywiki-settings',
    },
    {
        'file': os.path.join(basedir,'en.license.md'),
        'language': 'en',
        'title': "TinyWiki License",
        'slug': 'en-tinywiki-license',
    },
    # German Pages
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
                'builtin_id': -1000,
                'file': os.path.join(basedir,'Lama.jpg'),
                'alt': "Bild von einem Lama",
                'description': "Ein Testbild",
                'sidebar': True,
            },
            {
                'builtin_id': -1001,
                'file': os.path.join(basedir,'vineyard-styria.jpg'),
                'alt': "Sterischer Weinberg",
                'description': "Ein Weinberg in der Stierermark.",
                'sidebar': True,
            }
        ],
    },
    {
        'file': os.path.join(basedir,'de.settings.md'),
        'language':'de',
        'title': 'TinyWiki Einstellungen',
        'slug': "de-tinywiki-settings",
    }
]
