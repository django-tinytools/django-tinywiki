from .. import settings
from .. import models
from ..builtin_wiki_pages import BUILTIN_PAGES

from django.contrib.auth.models import Group,Permission
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string

import os
from pathlib import Path

from .wiki import install_builtin_wiki_page

def init_tinywiki_user():
    UserModel = get_user_model()
    try:
        if "email" in settings.TINYWIKI_USER:
            user = UserModel.objects.get(email=settings.TINYWIKI_USER["email"])
        elif "username" in settings.TINYWIKI_USER:
            user = UserModel.objects.get(username=settings.TINYWIKI_USER["username"])
        else:
            raise LookupError("Unable to find TinyWiki user! (\"email\" and \"username\" is missing!)")
    except UserModel.DoesNotExist:
        user = UserModel.objects.create(**settings.TIYNWIKI_USER)
        user.password = get_random_string(length=64)
        user.save()

    return user

def init_languages():
    for lcode,lname in settings.TINYWIKI_LANGUAGES:
        try:
            lang = models.WikiLanguage.objects.get(code=lcode)
            lang.name = lname
            lang.is_builtin = True
            lang.save()
            print("[django-tinywiki] Language \"{lang_code}\": \"{lang_name}\" updated".format(
                  lang_code=lang.code,
                  lang_name=lang.name))
        except models.WikiLanguage.DoesNotExist:
            lang = models.WikiLanguage.objects.create(code=lcode,name=lname,is_builtin=True)
            print("[django-tinywiki] Language \"{lang_code}\": \"{lang_name}\" created".format(
                  lang_code=lang.code,
                  lang_name=lang.name))

def init_groups():
    for group,permissions in settings.TINYWIKI_GROUPS:
        try:
            grp = Group.objects.get(name=group)
        except Group.DoesNotExist:
            grp = Group.objects.create(name=group)
            print("[django-tinywiki] Group \"{group}\" added".format(group=grp.name))
        
        if permissions:
            for p in grp.permissions.all():
                if p.codename not in permissions:
                    p.delete()

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

def init_media_dirs():
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
    if not user.is_authenticated or not user.is_superuser:
        raise PermissionError("User is not authenticated or not a superuser!")

    tw_user = init_tinywiki_user()
    init_languages()
    init_groups()
    init_media_dirs()
    
    if tw_user is None:
        tw_user = user

    for p in BUILTIN_PAGES:
        wp = install_builtin_wiki_page(tw_user,**p)
