# TinyWiki Settings

## Table of Contents

[TOC]

## Generic Settings

### Version

#### TINYWIKI_VERSION

This is a read only settings giving the current version of *django-tinywiki*.

### Application Settings

#### TINYWIKI_TITLE

The title displayed in the header bar. Set this to your Wiki/Site name when
using the tinywiki base html template.

``` { .python }
TINYWIKI_TITLE = "TinyWiki"
```

#### TINYWIKI_STYLE

``` { .python }
TINYWIKI_STYLE = "default"
```
#### TINYWIKI_CSS

``` { .python }
TINYWIKI_CSS = "{url}django_tinywiki/styles/{style}.css".format(
    url=STATIC_URL,
    style=TINYWIKI_STYLE)
```
#### TINYWIKI_CODEHILITE_STYLE

``` { .python }
TINYWIKI_CODEHILITE_STYLE = "github-dark"
```

#### TINYWIKI_CODEFHILITE_CSS

``` { .python }
TINYWIKI_CODEHILITE_CSS = "{url}django_tinywiki/styles/codehilite/{style}.css".format(
    url=STATIC_URL,
    style=TINYWIKI_CODEHILITE_STYLE)
```

#### TINYWIKI_MARKDOWN_EXTENSIONS

``` { .python }
TINYWIKI_MARKDOWN_EXTENSIONS = [MarkdowExtension1(),"path.to:MarkdownExtension2"]
```

#### TINYWIKI_CONTEXT_CALLBACK

``` { .python }
def context_function(request):
    context = {
        'context_variable':'value',
    }
    return context

TINYWIKI_CONTEXT_CALLBACK = context_function
```

You can also specify the context function as a string:

``` { .python }
TINYWIKI_CONTEXT_CALLBACK = "path.to.context_function"
```

#### TINYWIKI_DEFAULT_LANGUAGE

``` { .python }
TINYWIKI_DEFAULT_LANGUAGE = "en"
```

#### TINYWIKI_USER

This is the username used to assign the TinyWiki builtin pages to.
Set this to a dictionary that can be used as *kwargs* for creating
the username with the *AUTH_USER_MODEL* model.

``` { .python }
TINYWIKI_USER = {
    'username':'TinyWikiTeam',
    'email': 'tinywiki@cmoser.eu',
    'first_name':'TinyWiki',
    'last_name':'Team',
}
```

#### TINYWIKI_LEFT_SIDEBAR_FUNCTION

``` { .python }
def left_sidebar_function(request):
    sidebar = [
        {
            'title': "My Title",
            'items': [
                {
                    'title': _('Main Page'),
                    'page': "en-tinywiki-index",
                },
                {
                    'title': "A link",
                    'url': 'https://www.google.com',
                },
                {
                    'widget': '<a href="https://www.google.com">Google</a>',
                }
            ]
        },
    ]
    return sidebar

TINYWIKI_LEFT_SIDEBAR_FUNCTION = "path.to.left_sidebar_function"
```

#### TINYWIKI_RIGHT_SIDEBAR_FUNCTION

``` { .python }
def right_sidebar_function(request):
    return [
        '<div class="right-sidebar-item">Sidebar Item0.</div>',
        '<div class="right-sidebar-item">Sidebar Item2</div>'
    ]

TINYWIKI_RIGHT_SIDEBAR_FUNCTION = "path.to.right_sidebar_function"
```

### WIKI Images

#### TINYWIKI_IMAGE_WIKI_WIDTH

This defines the maximum width of Images displayed in a Wiki Page.
Bigger images are resized to have the maximum width defined here.
This should speed up loading pages with many images or big images.

``` { .pyhton }
TINYWIKI_IMAGE_WIKI_WIDTH = 860
```

#### TINYWIKI_IMAGE_PREVIEW_WIDTH

The maximum preview width of the image. This should speed up loading of
preview images in a page. If you are allowed to edit a page, a *Linked Images*
section is shown in Wiki-Pages with image previews or with the 
```[WIKI-IMAGES]``` tag in the wiki markdown. The images shown in there do not
neccessarily need to be shown in the page or in the sidebar.

This should speed up loading of the page and save some web traffic.

``` { .pyhton }
TINYWIKI_IMAGE_PREVIEW_WIDTH = 240
```

#### TINYWIKI_IMAGE_SIDEBAR_WIDTH

This setting defines the maximum width of images shown in the sidebar.
Set this to a reasonable if you have sidebar images enabled.

``` { .python }
TINYWIKI_IMAGE_SIDEBAR_WIDTH = 240
```

### Project Settings

#### TINYWIKI_IS_MAIN_APP

Set this value to ```True``` if TinyWiki is run in standalone mode,
```False``` otherwise.

``` { .python }
TINYWIKI_IS_MAIN_APP = False
```

## URL Settings

### Wiki Urls

#### TINYWIKI_INDEX

Then index page of TinyWiki. This should be an url pointing to the index
page of *django_tinywiki*.

``` { .python }
 from django.urls import reverse_lazy

 TINYWIKI_INDEX = reverse_lazy("tinywiki:index")
```

#### TINYWIKI_HOME_URL

The URL of the homepage of the Site. (This setting is currently unused, but
planned to be used in the future!)

``` { .python }
TINYWIKI_INDEX = "/"
```

#### TINYWIKI_PAGE_VIEW_URL_TEMPLATE

If you want to use your own view for rendering *TinyWiki*-pages you can set
this setting to an appropriate value. The set url template is looked up by 
```reverse(TINYWIKI_PAGE_VIEW_URL_TEMPLATE,kwargs={"page":"slug-for-page"})```.

``` { .python }
TINYWIKI_PAGE_VIEW_URL_TEMPLATE = "tinywiki:page"
```
#### TINYWIKI_PAGE_EDIT_URL_TEMPLATE

If you are using your own view for editing wiki-pages, set this vairable to
the view you are using.

``` { .python }
TINYWIKI_PAGE_EDIT_URL_TEMPLATE = "tinywiki:page-edit"

```
#### TINYWIKI_PAGE_CREATE_URL_TEMPLATE

#### TINYWIKI_PAGE_NEW_URL_TEMPLATE

#### TINYWIKI_PAGE_DELETE_URL_TEMPLATE

#### TINYWIKI_PAGE_OVERVIEW_URL

### Project URLs

#### TINYWIKI_LOGIN_URL

This is the login url of the wiki. To ```reverse_lazy("tinywiki:auth-login")```
if TinyWiki is the main application, else it is set to the setting *LOGIN_URL*.

``` { .python }
TINYWIKI_LOGIN_URL = "/login/"
```

#### TINYWIKI_LOGOUT_URL

This setting defines the logout-URL of the site. If TinyWiki is the main
application it defaults to ```reverse_lazy("tinywiki:auth-logout")``` 
else it is set to the setting *LOGOUT_URL*.

``` { .python }
TINYWIKI_LOGOUT_URL = "/logout/"
```

#### TINYWIKI_SIGNUP_URL

This setting deines the *Sign Up*-URL of the site. If TinyWiki is the main
application it defaults to ```reverse_lazy("tinywiki:auth-signup")```, else
it it set to the setting *SIGNUP_URL*.

``` { .python }
TINYWIKI_SIGNUP_URL = "/singup/"
```

## Template Settings

### Wiki Templates

#### TINYWIKI_BASE_TEMPLATE

This setting defines the base template to be extended by *TinyWiki*.
You can set write your own template and override the default page
layout of *TinyWiki*.

``` { .python }
TINYWIKI_BASE_TEMPLATE = "django_tinywiki/base.html"
```

#### TINYWIKI_PAGE_VIEW_TEMPLATE

You can define yourself how Wiki-Pages are displayed by using this setting.
The ```content``` context variable contains the rendered markdown for the
page.

``` { .python }
TINYWIKI_PAGE_VIEW_TEMPLATE = "django_tinywiki/wiki/page.html"
```

#### TINYWIKI_PAGE_EDIT_TEMPLATE

Set this variable to your template file, if you want to use your own
template for the edit page.

``` { .python }
TINYWIKI_PAGE_EDIT_TEMPLATE = "django_tinywiki/wiki/edit.html"
```

#### TINYWIKI_PAGE_CREATE_TEMPLATE

#### TINYWIKI_PAGE_NEW_TEMPLATE

#### TINYWIKI_PAGE_DELETE_TEMPLATE

#### TINYWIKI_PAGE_DELETE_DONE_TEMPLATE

#### TINYWIKI_PAGE_OVERVIEW_TEMPLATE

