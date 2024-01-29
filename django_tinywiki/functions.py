from . import settings
from .models import WikiLanguage,WikiPage,WikiPageBackup
from .builtin_wiki_pages import BUILTIN_PAGES

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.template import Context,Template
import sys
import os

import markdown


def init_app(user):
    def init_wiki_media_directories():
        directories= [
            'images/wiki/original',
            'images/wiki/view',
            'images/wiki/preview',
            'images/wiki/sidebar'
        ]
        root_dir = settings.TINYWIKI_MEDIA_ROOT
        for i in directories:
            directory = os.path.join(root_dir,i)
            if not os.path.exists(directory):
                os.makedirs(directory)
                print("[mkdir] {}".format(directory))
    
    def init_languages():
        for lcode,lname in settings.TINYWIKI_LANGUAGES:
            try:
                lang = WikiLanguage.objects.get(code=lcode)
                lang.name = lname
                lang.is_builtin = True
                lang.save()
                print("[django-tinywiki] Language \"{lang_code}\": \"{lang_name}\" updated".format(
                    lang_code=lang.code,
                    lang_name=lang.name))
            except WikiLanguage.DoesNotExist:
                lang = WikiLanguage.objects.create(code=lcode,name=lname,is_builtin=True)
                print("[django-tinywiki] Language \"{lang_code}\": \"{lang_name}\" created".format(
                    lang_code=lang.code,
                    lang_name=lang.name))

    def init_groups():
        for group in settings.TINYWIKI_GROUPS:
            try:
                grp = Group.objects.get(name=group)
            except Group.DoesNotExist:
                grp = Group.objects.create(name=group)
                print("[django-tinywiki] Group \"{group}\" added".format(group=grp.name))

    def install_tinywiki_pages():
        for spec in BUILTIN_PAGES:
            try:
                lang = WikiLanguage.objects.get(code=spec['language'])
            except WikiLanguage.DoesNotExist:
                continue

            if not os.path.isfile(spec['file']):
                continue

            with open(spec['file'],"r") as content_file:
                content = content_file.read()

            try:
                page = WikiPage.objects.get(slug=spec['slug'])
                page_update = False
                backup_kwargs = {
                    'wiki_page': page,
                    'slug': page.slug,
                    'title': page.title,
                    'language': page.language,
                    'content': page.content,
                    'created_on': page.created_on,
                    'created_by': page.created_by,
                    'edited_on': page.edited_on,
                    'edited_by': page.edited_by,
                    'edited_reason': page.edited_reason,
                }

                if page.title != spec['title']:
                    page.title = spec['title']
                    page_update = True
                if page.content != content:
                    page.content = content
                    page_update = True

                if page_update:
                    WikiPageBackup.objects.create(**backup_kwargs)
                    page.edited_reason="Update"
                    page.edited_by=user
                    page.save()
                    print("[django-tinywiki] Page \"{slug}\" updated".format(slug=page.slug))

            except WikiPage.DoesNotExist:
                page = WikiPage.objects.create(
                    slug=spec['slug'],
                    language=lang,
                    title=spec['title'],
                    content=content,
                    created_by=user,
                    edited_by=user,
                    edited_reason="",
                    userlock=True,
                    editlock=True
                )
                print("[django-tinywiki] Page \"{slug}\" created".format(slug=page.slug))

    if not user.is_superuser:
        raise RuntimeError(
            "Unable to initialize \"django-tinywiki\" because user \"{user}\" is not a superuser!".format(user=user))

    init_wiki_media_directories()
    init_languages()
    init_groups()
    install_tinywiki_pages()
    

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
    return markdown_to_html(t.render(c))
