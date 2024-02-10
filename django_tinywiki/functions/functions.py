from .. import settings
from ..models import WikiLanguage,WikiPage,WikiPageBackup,WikiImage
from ..builtin_wiki_pages import BUILTIN_PAGES

from django.contrib.auth.models import Group,Permission
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.template import Context,Template
from django.core.files import File
import sys
import os
from pathlib import Path
from shutil import copyfile
import PIL
import markdown
import re


def user_can_create_pages(user):
    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True
    for group in user.group.all():
        if group.name in ['wiki-admin','wiki-author']:
            return True
    return False

def get_language_code(self):
    x = _("language-code")
    if x == "language-code":
        return "en"
    return x

def markdown_to_html(md_string):
    return markdown.markdown(md_string,extensions=settings.TINYWIKI_MARKDOWN_EXTENSIONS)

def render_markdown(string,context=None):
    if context is None:
        context={}

    c = Context(context)
    t = Template(string)
    if context and 'slug' in context:
        slug = context['slug']
    else:
        slug = None

    if context and 'edit_page' in context:
        edit_page = context['edit_page']
    else:
        edit_page = False
        

    s = t.render(c)
    return markdown.markdown(s,extensions=settings.TINYWIKI_MARKDOWN_EXTENSIONS,
                             extension_configs={
                                "django_tinywiki.markdown_extensions:TinywikiLinkedImagesExtension": {
                                   'wiki_page': slug,
                                   'edit_page': edit_page,
                               }
                            })

def user_is_superuser(user):
    return (user and user.is_authenticated and user.is_superuser)
