from . import settings
from .models import WikiLanguage,WikiPage,WikiPageBackup,WikiImage
from .builtin_wiki_pages import BUILTIN_PAGES

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

def _init_languages():
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

def _init_groups():
    for group,permissions in settings.TINYWIKI_GROUPS:
        try:
            grp = Group.objects.get(name=group)
        except Group.DoesNotExist:
            grp = Group.objects.create(name=group)
            print("[django-tinywiki] Group \"{group}\" added".format(group=grp.name))
        
        if permissions:
            for p in [i.codename for i in grp.permissions.all()]:
                if p not in permissions:
                    grp.permissions.delete()

            for perm in permissions:
                if not grp.permissions.filter(codename=perm):
                    try:
                        p = Permission.objects.get(codename=perm)
                        grp.permissions.add(p)
                        print("Permissions {permission} added to Group {group}".format(permission=perm,group=grp.name))
                    except Permission.DoesNotExist:
                        pass
        else:
            grp.permissions.clear()


def _init_media_dirs():
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

def init_app(user):
    def install_tinywiki_pages(user):
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

            with open(spec['file'],"r",encoding="utf-8") as content_file:
                content = content_file.read()

            try:
                page = WikiPage.objects.get(slug=spec['slug'])
                page_update = False
                backup_kwargs = {
                    'wiki_page': page,
                    'slug': page.slug,
                    'title': page.title,
                    'language': page.language,
                    'user': page.user,
                    'content': page.content,
                    'created_on': page.created_on,
                    'created_by': page.created_by,
                    'edited_on': page.edited_on,
                    'edited_by': page.edited_by,
                    'edited_reason': page.edited_reason,
                }

                if page.user != user:
                    page.user = user
                    page_update = True
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
                        if not os.path.isfile(from_file):
                            continue
                    except:
                        continue
                    
                    root_dir = Path(settings.TINYWIKI_IMAGE_UPLOAD_DIRECTORY)
                    if not os.path.exists(root_dir):
                        os.makedirs(root_dir)

                    try:
                        wi = WikiImage.objects.get(builtin_id=builtin_id)
                    except WikiImage.DoesNotExist:
                        fname = os.path.basename(from_file)
                        if os.path.splitext(fname)[1] == 'svg':
                            convert = False
                        else:
                            convert = True

                        new_fname = "builtin.{}{}".format(builtin_id,os.path.splitext(fname)[1])
                        original_path = os.path.join(settings.TINYWIKI_IMAGE_UPLOAD_DIRECTORY,("original." + new_fname))
                        wiki_path = os.path.join(settings.TINYWIKI_IMAGE_UPLOAD_DIRECTORY,("wiki." + new_fname))
                        sidebar_path = os.path.join(settings.TINYWIKI_IMAGE_UPLOAD_DIRECTORY,("sidebar." + new_fname))
                        preview_path = os.path.join(settings.TINYWIKI_IMAGE_UPLOAD_DIRECTORY,("preview." + new_fname))

                        copyfile(from_file,original_path)
                        
                        img = PIL.Image.open(original_path)
                        width,height = img.size
                        

                        if convert and img.width > settings.TINYWIKI_IMAGE_WIKI_WIDTH:
                            new_size = (settings.TINYWIKI_IMAGE_WIKI_WIDTH,
                                        int((height * (settings.TINYWIKI_IMAGE_WIKI_WIDTH / width)) + 0.5))
                            wiki_img = img.resize(new_size)
                            wiki_img.save(wiki_path)
                            wiki_img.close()
                        else:
                            copyfile(from_file,wiki_path)

                        if width > settings.TINYWIKI_IMAGE_PREVIEW_WIDTH:
                            new_size = (settings.TINYWIKI_IMAGE_PREVIEW_WIDTH,
                                        int((height * (settings.TINYWIKI_IMAGE_PREVIEW_WIDTH / width)) + 0.5))
                            prev_img = img.resize(new_size)
                            prev_img.save(preview_path)
                            prev_img.close()
                        else:
                            copyfile(from_file,preview_path)

                        if width > settings.TINYWIKI_IMAGE_SIDEBAR_WIDTH:
                            new_size = (settings.TINYWIKI_IMAGE_SIDEBAR_WIDTH,
                                        int((height * (settings.TINYWIKI_IMAGE_SIDEBAR_WIDTH / width)) + 0.5))
                            sidebar_img = img.resize(new_size)
                            sidebar_img.save(sidebar_path)
                            sidebar_img.close()
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
                        img.close()
                        for img_path in [sidebar_path,preview_path,wiki_path,original_path]:
                            if os.path.isfile(img_path):
                                os.unlink(img_path)

                    re_pattern = "\!\[\[\-\-[\-]?{}\-\-\]\]".format(builtin_id)
                    recp = re.compile(re_pattern)
                    page.content = re.sub(recp,"![[{}]]".format(wi.id),page.content)
                    page.save()


    if not user.is_superuser:
        raise RuntimeError(
            "Unable to initialize \"django-tinywiki\" because user \"{user}\" is not a superuser!".format(user=user))

    _init_languages()
    _init_groups()
    _init_media_dirs()

    UserModel = get_user_model()
    try:
        tw_user = UserModel.objects.get(username=settings.TINYWIKI_USER["username"])
    except UserModel.DoesNotExist:
        tw_user = user
    
    install_tinywiki_pages(tw_user)
    

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
