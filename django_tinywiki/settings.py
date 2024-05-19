from django.conf import settings as django_settings
from django.contrib.auth.models import User as UserModel
from django.utils.translation import gettext_lazy as _, gettext_noop as N_
from django.utils.module_loading import import_string
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

import os

from .version import TINYWIKI_VERSION

TINYWIKI_PACKAGE = os.path.basename(os.path.dirname(__file__))
TINYWIKI_APP = TINYWIKI_PACKAGE

TINYWIKI_IS_MAIN_APP = getattr(django_settings,"TINYWIKI_IS_MAIN_APP",False)

TINYWIKI_TITLE = getattr(django_settings,"TINYWIKI_TITLE",_("TinyWiki"))

TINYWIKI_INDEX = getattr(django_settings,
                         "TINYWIKI_INDEX",
                         _("en-tinywiki-index"))

TINYWIKI_HOME_URL = getattr(django_settings,"TINYWIKI_HOME_URL","/")

TINYWIKI_BASE_TEMPLATE = getattr(django_settings,
                                 "TINYWIKI_BASE_TEMPLATE",
                                 "django_tinywiki/base.html")
TINYWIKI_PAGE_VIEW_TEMPLATE = getattr(django_settings,
                                      "TINYWIKI_PAGE_VIEW_TEMPLATE",
                                      "django_tinywiki/wiki/page.html")
TINYWIKI_PAGE_VIEW_URL_TEMPLATE = getattr(django_settings,"TINYWIKI_PAGE_VIEW_URL","tinywiki:page")
TINYWIKI_PAGE_EDIT_TEMPLATE = getattr(django_settings,
                                      "TINYWIKI_PAGE_EDIT_TEMPLATE",
                                      "django_tinywiki/wiki/edit.html")
TINYWIKI_PAGE_EDIT_URL_TEMPLATE = getattr(django_settings,"TINYWIKI_PAGE_EDIT_URL_TEMPLATE","tinywiki:page-edit")

TINYWIKI_PAGE_OVERVIEW_URL = getattr(django_settings,"TINYWIKI_PAGE_OVERVIEW_URL",reverse_lazy("tinywiki:page-overview"))
TINYWIKI_PAGE_OVERVIEW_TEMPLATE = getattr(django_settings,"TINYWIKI_PAGE_OVERVIEW_TEMPLATE","django_tinywiki/wiki/overview.html")

TINYWIKI_PAGE_CREATE_TEMPLATE = getattr(django_settings,
                                        "TINYWIKI_PAGE_CREATE_TEMPLATE",
                                        "django_tinywiki/wiki/create.html")
TINYWIKI_PAGE_CREATE_URL_TEMPLATE = getattr(django_settings,"TINYWIKI_PAGE_CREATE_URL_TEMPLATE","tinywiki:page-create")
TINYWIKI_PAGE_NEW_TEMPLATE = getattr(django_settings,
                                     "TINYWIKI_PAGE_NEW_TEMPLATE",
                                     TINYWIKI_PAGE_CREATE_TEMPLATE),
TINYWIKI_PAGE_NEW_URL = getattr(django_settings,'TINYWIKI_PAGE_NEW_URL_TEMPLATE',reverse_lazy('tinywiki:page-new'))

TINYWIKI_PAGE_DELETE_URL_TEMPLATE = getattr(django_settings,"TINYWIKI_PAGE_DELETE_URL_TEMPLATE","tinywiki:page-delete")
TINYWIKI_PAGE_DELETE_TEMPLATE = getattr(django_settings,"TINYWIKI_PAGE_DELETE_TEMPLATE","django_tinywiki/wiki/delete.html")
TINYWIKI_PAGE_DELETE_DONE_TEMPLATE = getattr(django_settings,"TINYWIKI_PAGE_DELETE_DONE_TEMPLATE","django_tinywiki/wiki/delete-done.html")

TINYWIKI_STYLE = getattr(django_settings,
                         "TINYWIKI_STYLE",
                         "default")
TINYWIKI_CSS = getattr(django_settings,
                       "TINYWIKI_CSS",
                       "{url}django_tinywiki/styles/{style}.css".format(
                            url=django_settings.STATIC_URL,
                            style=TINYWIKI_STYLE))
TINYWIKI_CODEHILITE_STYLE = getattr(django_settings,
                                    "TINYWIKI_CODEHILITE_STYLE",
                                    "github-dark")
TINYWIKI_CODEHILITE_CSS = getattr(django_settings,
                                  "TINYWIKI_CODEHILITE_CSS",
                                  "{url}django_tinywiki/styles/codehilite/{style}.css".format(
                                      url=django_settings.STATIC_URL,
                                      style=TINYWIKI_CODEHILITE_STYLE))

TINYWIKI_MARKDOWN_EXTENSIONS = getattr(django_settings,
                                       "TINYWIKI_MARKDOWN_EXTENSIONS",
                                       None)
TINYWIKI_CONTEXT_CALLBACK = getattr(django_settings,
                                    "TINYWIKI_CONTEXT_CALLBACK",
                                    None)

TINYWIKI_DEFAULT_LANGUAGE = getattr(django_settings,"TINYWIKI_DEFAULT_LANGUAGE","en")

if not hasattr(django_settings,"MEDIA_URL"):
    django_settings.MEDIA_URL = "/media"

TINYWIKI_MEDIA_ROOT = getattr(django_settings,
                              "TINYWIKI_MEDIA_ROOT",
                              os.path.join(
                                  getattr(django_settings,'MEDIA_ROOT',
                                          django_settings.BASE_DIR / "media"),'wiki'))
TINYWIKI_MEDIA_URL = getattr(django_settings,
                             "TINYWIKI_MEDIA_URL",
                             django_settings.MEDIA_URL + "wiki/")

TINYWIKI_UPLOAD_ROOT = getattr(django_settings,"TINYWIKI_UPLOAD_ROOT",django_settings.BASE_DIR / '.uploads')
TINYWIKI_IMAGE_UPLOAD_URL = getattr(django_settings,
                                    "TINYWIKI_IMAGE_UPLOAD_URL",
                                    'tinywiki:image-upload')
TINYWIKI_IMAGE_UPLOAD_TEMPLATE = getattr(django_settings,
                                         "TINYWIKI_IMAGE_UPLOAD_TEMPLATE",
                                         'django_tinywiki/wiki/image-upload.html')
TINYWIKI_IMAGE_UPLOAD_DIRECTORY = getattr(django_settings,
                                          "TINYWIKI_IMAGE_UPLOAD_DIRECTORY",
                                          os.path.join(TINYWIKI_UPLOAD_ROOT,'wiki-images'))

TINYWIKI_MEDIA_STORAGE = getattr(django_settings,
                                 "TINYWIKI_MEDIA_STORAGE",
                                 FileSystemStorage(location=TINYWIKI_MEDIA_ROOT,
                                                   base_url=TINYWIKI_MEDIA_URL))

TINYWIKI_IMAGE_WIKI_WIDTH = getattr(django_settings,"TINYWIKI_IMAGE_WIKI_WIDTH",860)
TINYWIKI_IMAGE_PREVIEW_WIDTH = getattr(django_settings,"TINYWIKI_IMAGE_PREVIEW_WIDTH",240)
TINYWIKI_IMAGE_SIDEBAR_WIDTH = getattr(django_settings,"TINYWIKI_IMAGE_SIDEBAR_WIDTH",200)

TINYWIKI_AUTH_USER_MODEL = getattr(django_settings,
                                   "TINYWIKI_AUTH_USER_MODEL",
                                   getattr(django_settings,"AUTH_USER_MODEL","django.contrib.auth.models.User"))

TINYWIKI_SIGNUP_TEMPLATE = getattr(django_settings,"TINYWIKI_SIGNUP_TEMPLATE","django_tinywiki/auth/signup.html")
TINYWIKI_SIGNUP_SUCCESS_TEMPLATE = getattr(django_settings,"TINYWIKI_SIGNUP_SUCCESS_TEMPLATE","django_tinywiki/auth/signup-success.html")

if TINYWIKI_IS_MAIN_APP:
    TINYWIKI_LOGIN_URL = getattr(django_settings,
                                "TINYWIKI_LOGIN_URL",
                                getattr(django_settings,'LOGIN_URL',reverse_lazy("tinywiki:auth-login")))
    TINYWIKI_SIGNUP_URL = getattr(django_settings,
                                  "TINYWIKI_SIGNUP_URL",
                                  getattr(django_settings,"SIGNUP_URL",reverse_lazy("tinywiki:auth-signup")))
    TINYWIKI_LOGOUT_URL = getattr(django_settings,
                                  "TINYWIKI_LOGOUT_URL",
                                  getattr(django_settings,"LOGOUT_URL",reverse_lazy("tinywiki:auth-logout")))
else:
    TINYWIKI_LOGIN_URL = getattr(django_settings,"TINYWIKI_LOGIN_URL",getattr(django_settings,"LOGIN_URL","/login/"))
    TINYWIKI_SIGNUP_URL = getattr(django_settings,"TINYWIKI_SIGNUP_URL",getattr(django_settings,"SIGNUP_URL","/signup/"))
    TINYWIKI_LOGOUT_URL = getattr(django_settings,"TINYWIKI_LOGOUT_URL",getattr(django_settings,"LOGOUT_URL","/logout/"))

BUILTIN_TINYWIKI_USER = {"username":"TinyWikiTeam","email":"tinywiki@cmoser.eu","first_name":"TinyWiki","last_name":"Team"}
TINYWIKI_USER = getattr(django_settings,"TINYWIKI_USER",BUILTIN_TINYWIKI_USER)


TINYWIKI_RIGHT_SIDEBAR_FUNCTION = getattr(django_settings,"TINYWIKI_RIGHT_SIDEBAR_FUNCTION",None)

RIGHT_SIDEBAR_FUNCTION = getattr(django_settings,
                                 "RIGHT_SIDEBAR_FUNCTION",
                                 "django_tinywiki.functions.sidebar.render_right_sidebar")


TINYWIKI_GROUP_ADMIN = "tinywiki-admin"
TINYWIKI_GROUP_AUTHOR = "tinywiki-author"
TINYWIKI_GROUP_USER = "tinywiki-user"

TINYWIKI_PERM_CREATE_PAGE = "tinywiki-create-page"
TINYWIKI_PERM_DELETE_PAGE = "tinywiki-delete-page"
TINYWIKI_PERM_EDIT_PAGE = "tinywiki-edit-page"
TINYWIKI_PERM_EDIT_USER_PAGE = "tinywiki-edit-user-page"
TINYWIKI_PERM_ADMIN = "tinywiki-admin"

TINYWIKI_DEFAULT_GROUPS = getattr(django_settings,"TINYWIKI_DEFAULT_GROUPS",[TINYWIKI_GROUP_AUTHOR,TINYWIKI_GROUP_USER])

TINYWIKI_APPNAME = "django_tinywiki"

TINYWIKI_LANGUAGES = [
    ("en",N_("English")),
    ("de",N_("German")),
]

TINYWIKI_STAFF_IS_WIKI_ADMIN = getattr(django_settings,"TINYWIKI_STAFF_IS_WIKI_ADMIN",False)
TINYWIKI_SUPERUSER_IS_WIKI_ADMIN = getattr(django_settings,"TINYWIKI_SUPERUSER_IS_WIKI_ADMIN",True)

TINYWIKI_LEFT_SIDEBAR_FUNCTION = getattr(django_settings,"TINYWIKI_LEFT_SIDEBAR_FUNCTION",None)
TINYWIKI_LEFT_SIDEBAR_DATA = getattr(django_settings,"TINYWIKI_LEFT_SIDEBAR_DATA",None)
TINYWIKI_SHOW_TINYWIKI_LEFT_SIDEBAR_ITEMS = getattr(django_settings,"TINYWIKI_SHOW_TINYWIKI_LEFT_SIDEBAR_ITEMS",True)

LEFT_SIDEBAR_FUNCTION = getattr(django_settings,"LEFT_SIDEBAR_FUNCTION",'django_tinywiki.functions.sidebar.render_left_sidebar')

# allow mulitple instances of tinywiki in one prjeoct by overriding app based settings
# !!!DO THIS ONLY WHEN YOU KNOW WHAT YOU ARE DOING!!!
if os.path.isfile(os.path.join(os.path.dirname(__file__),"tinywiki_settings.py")):
    from .tinywiki_settings import *

__mkperm = lambda x: "{}.{}".format(TINYWIKI_APPNAME,x)

TINYWIKI_GROUPS = [
    (TINYWIKI_GROUP_ADMIN,[TINYWIKI_PERM_CREATE_PAGE,
                           TINYWIKI_PERM_DELETE_PAGE,
                           TINYWIKI_PERM_EDIT_PAGE,
                           TINYWIKI_PERM_EDIT_USER_PAGE,
                           TINYWIKI_PERM_ADMIN]),
    (TINYWIKI_GROUP_AUTHOR,[TINYWIKI_PERM_CREATE_PAGE,
                            TINYWIKI_PERM_EDIT_PAGE,
                            TINYWIKI_PERM_EDIT_USER_PAGE]),
    (TINYWIKI_GROUP_USER,[TINYWIKI_PERM_EDIT_USER_PAGE]),
]

BUILTIN_MARKDOWN_EXTENSIONS = [
    "toc",
    "codehilite",
    "fenced_code",
    "tables",
    "django_tinywiki.markdown_extensions:DjangoURLExtension",
    "django_tinywiki.markdown_extensions:TinywikiImageExtension",
    "django_tinywiki.markdown_extensions:TinywikiLinkedImagesExtension",
    "django_tinywiki.markdown_extensions:TinywikiLinkExtension",
    "django_tinywiki.markdown_extensions:DelExtension",
    "django_tinywiki.markdown_extensions:CopyrightExtension",
    "django_tinywiki.markdown_extensions.video:VideoExtension",
]

# snaitize context callback
if TINYWIKI_CONTEXT_CALLBACK is None:
    TINYWIKI_CONTEXT_CALLBACK = lambda self,x: {}
elif isinstance(TINYWIKI_CONTEXT_CALLBACK,str):
    TINYWIKI_CONTEXT_CALLBACK = import_string(TINYWIKI_CONTEXT_CALLBACK)

if not callable(TINYWIKI_CONTEXT_CALLBACK):
    raise ValueError("Option \"TINYWIKI_CONTEXT_CALLBACK\" does not result in a callable function!")

if TINYWIKI_MARKDOWN_EXTENSIONS is None:
    TINYWIKI_MARKDOWN_EXTENSIONS = BUILTIN_MARKDOWN_EXTENSIONS
else:
    TINYWIKI_MARKDOWN_EXTENSIONS = list(TINYWIKI_MARKDOWN_EXTENSIONS) + BUILTIN_MARKDOWN_EXTENSIONS

TINYWIKI_USERPERM_ADMIN = '.'.join((TINYWIKI_PACKAGE,TINYWIKI_PERM_ADMIN))
TINYWIKI_USERPERM_CREATE_PAGE = '.'.join((TINYWIKI_PACKAGE,TINYWIKI_PERM_CREATE_PAGE))
TINYWIKI_USERPERM_DELETE_PAGE = '.'.join((TINYWIKI_PACKAGE,TINYWIKI_PERM_DELETE_PAGE))
TINYWIKI_USERPERM_EDIT_PAGE = '.'.join((TINYWIKI_PACKAGE,TINYWIKI_PERM_EDIT_PAGE))
TINYWIKI_USERPERM_EDIT_USER_PAGE = '.'.join((TINYWIKI_PACKAGE,TINYWIKI_PERM_EDIT_USER_PAGE))
