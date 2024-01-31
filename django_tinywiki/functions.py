from . import settings
from .models import WikiLanguage,WikiPage,WikiPageBackup,WikiImage
from .builtin_wiki_pages import BUILTIN_PAGES

from django.contrib.auth.models import Group
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

    def create_media_dirs():
        root_dir = Path(settings.TINYWIKI_MEDIA_ROOT)
        directories = [
            root_dir / "upload" / "images",
            root_dir / "images" / "original",
            root_dir / "images" / "wiki",
            root_dir / "images" / "preview",
            root_dir / "images" / "sidebar",
        ]

        for d in directories:
            if not os.path.isdir(d):
                os.makedirs(d)

    def install_tinywiki_pages():
        pages = BUILTIN_PAGES
        if settings.TINYWIKI_BUILTIN_PAGES:
            pages += settings.TINYWIKI_BUILTIN_PAGES

        for spec in pages:
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

            media_root = Path(settings.TINYWIKI_MEDIA_ROOT)
            img_prefix = "images"

            if 'images' in spec:
                for img_spec in spec['images']:
                    try:
                        builtin_id = img_spec['builtin_id']
                        from_file = img_spec['file']
                        if 'alt' in img_spec:
                            alt = img_spec['alt']
                        else:
                            alt = None
                        if 'description' in img_spec:
                            desc = img_spec['description']
                        else:
                            desc = None
                    except:
                        continue
                    
                    print(builtin_id)

                    try:
                        wi = WikiImage.objects.get(builtin_id=builtin_id)
                    except WikiImage.DoesNotExist:
                        fname = os.path.basename(from_file)
                        new_fname = "builtin-{}{}".format(builtin_id,os.path.splitext(fname)[1])
                        original_path = media_root / img_prefix / "original" / new_fname
                        wiki_path = media_root / img_prefix / "wiki" / new_fname
                        sidebar_path = media_root / img_prefix / "sidebar" / new_fname
                        preview_path = media_root / img_prefix / "preview" / new_fname

                        copyfile(from_file,original_path)
                        img = PIL.Image.open(from_file)
                        width,height = img.size
                        img.close()

                        if img.width > settings.TINYWIKI_IMAGE_WIKI_WIDTH:
                            original_img = PIL.Image.open(from_file)
                            new_size = (settings.TINYWIKI_IMAGE_WIKI_WIDTH,
                                        int((height * (settings.TINYWIKI_IMAGE_WIKI_WIDTH / width)) + 0.5))
                            original_img.resize(new_size)
                            original_img.save(wiki_path)
                            original_img.close()
                        else:
                            copyfile(from_file,wiki_path)

                        if width > settings.TINYWIKI_IMAGE_PREVIEW_WIDTH:
                            original_img = PIL.Image.open(from_file)
                            new_size = (settings.TINYWIKI_IMAGE_PREVIEW_WIDTH,
                                        int((height * (settings.TINYWIKI_IMAGE_PREVIEW_WIDTH / width)) + 0.5))
                            original_img.resize(new_size)
                            original_img.save(preview_path)
                            original_img.close()
                        else:
                            copyfile(from_file,preview_path)

                        if width > settings.TINYWIKI_IMAGE_SIDEBAR_WIDTH:
                            original_img = PIL.Image.open(from_file)
                            new_size = (settings.TINYWIKI_IMAGE_SIDEBAR_WIDTH,
                                        int((height * (settings.TINYWIKI_IMAGE_SIDEBAR_WIDTH / width)) + 0.5))
                            original_img.resize(new_size)
                            original_img.save(sidebar_path)
                            original_img.close()
                        else:
                            copyfile(from_file,sidebar_path)

                        with open(original_path,'rb') as original_fp:
                            original_file = File(original_fp,name=new_fname)
                            wi = WikiImage.objects.create(wiki_page=page,alt=alt,description=desc,image=original_file,builtin_id=builtin_id)

                            with open(wiki_path,'rb') as wiki_fp:
                                wiki_file = File(wiki_fp,name=new_fname)
                                wi.image_wiki = wiki_file
                                wi.save()

                            with open(preview_path,'rb') as prev_fp:
                                prev_file = File(prev_fp,name=new_fname)
                                wi.image_preview = prev_file
                                wi.save()

                            with open(sidebar_path,'rb') as sidebar_fp:
                                sidebar_file = File(sidebar_fp,name=new_fname)
                                wi.image_sidebar = sidebar_file
                                wi.save()                      

                    re_pattern = "\!\[\[\-\-{}\-\-\]\]".format(builtin_id)
                    recp = re.compile(re_pattern)
                    page.content = re.sub(recp,"![[{}]]".format(wi.id),page.content)
                    page.save()


    if not user.is_superuser:
        raise RuntimeError(
            "Unable to initialize \"django-tinywiki\" because user \"{user}\" is not a superuser!".format(user=user))

    init_wiki_media_directories()
    init_languages()
    init_groups()
    create_media_dirs()
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
