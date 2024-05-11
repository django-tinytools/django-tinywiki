# TinyWiki Settings

## Table of Contents

[TOC]

## Generic Settings

### Version

#### TINYWIKI_VERSION

This is a read only setting giving the current version as a string of 
*django-tinywiki*.

### Package and App

#### TINYWIKI_PACKAGE

This is the readonly package name of *TinyWiki*. The name is dynamically
generated from the package directory.

#### TINYWIKI_APP

The read only name of the django application. Currently it is the same as
```TINYWIKI_PACKAGE```.


### Application Settings

#### TINYWIKI_TITLE

The title displayed in the header bar. Set this to your Wiki/Site name when
using the tinywiki base html template.

``` { .python }
TINYWIKI_TITLE = "TinyWiki"
```

#### TINYWIKI_STYLE

You can select the style of *TinyWiki* using the corresponding CSS-Stylesheet.

To show the available styles, run the *tinywiki_styles* script.

``` { .sh }
$ ./manage runscript tinywiki_styles
```

Set the *TINYWIKI_STYLE* variable to the style name of one of the available
styles. (Currently only the *default* style is supported).

``` { .python }
TINYWIKI_STYLE = "default"
```

#### TINYWIKI_CSS

If you have a CSS-Stylesheet for your application and you want to ignore the
style of the django-tinywiki, set the *TINYWIKI_CSS* variable to the 
stylesheet you are using.

``` { .python }
TINYWIKI_CSS = "/static/styles/my_style.css"
```
#### TINYWIKI_CODEHILITE_STYLE

You can change the codehilite style to one of the supported styles if you
want to change the look of the code sections of your wiki pages.

``` { .python }
TINYWIKI_CODEHILITE_STYLE = "github-dark"
```

To show all available styles, run the *tinywiki_codehilite_styles* script.

``` { .sh }
$ ./manage runscript tinywiki_codehilite_styles
```

#### TINYWIKI_CODEFHILITE_CSS

You can also import your own CSS-Stylesheet for the code sections in your
wiki pages by setting the *TINYWIKI_CODEHILITE_CSS* variable.

``` { .python }
TINYWIKI_CODEHILITE_CSS = "/static/styles/my_codehilite_style.css"
```

#### TINYWIKI_MARKDOWN_EXTENSIONS

You can import your own markdown extensions to be used for wiki pages, if needed.
To do this set the *TINYWIKI_MARKDOWN_EXTENSIONS* to a list of the extensions
to be loaded before processing the page.

There are more informations on
[Makrdown Extensions](https://python-markdown.github.io/extensions/) and on 
[writing Markdown Extensions](https://python-markdown.github.io/extensions/api/).

``` { .python }
TINYWIKI_MARKDOWN_EXTENSIONS = [MarkdowExtension1(),"path.to:MarkdownExtension2"]
```

#### TINYWIKI_CONTEXT_CALLBACK

This setting defines the context callback to be used for *TinyWiki*-views. This
setting might be useful when using your own templates and need to extend 
context variables.

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

The default language to use when creating *TinyWiki*-pages. The named 
language-code needs to be in the database or the fallback **en** is used.

``` { .python }
TINYWIKI_DEFAULT_LANGUAGE = "en"
```

#### TINYWIKI_LEFT_SIDEBAR

Set the left sidebar of *TinyWiki*. Set this to a list of 
sidebar-section-specifiers. The Layout of this settings-variable is shown in
the example. 

```TINYWIKI_LEFT_SIDEBAR``` is ment to be used for static sidebar content. If
you need to render a dynamic sidebar content, use 
```TINYWIKI_LEFT_SIDEBAR_FUNCTION``` variable to set the function to be called 
for creating the sidebar content for *TinyWiki* views.

``` { .python }
TINYWIKI_LEFT_SIDEBAR = [
    {
        'title': 'Sidebar Section',
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
```

#### TINYWIKI_LEFT_SIDEBAR_FUNCTION

Specify a function to be called for creating dynamic left sidebars.
The function is called with the ```request``` instance of the calling
view. This method is creating the content of *TinyWiki*-views.

The function should return a list of sidebar-section-specifiers. The
layout of the value to be returned is shown in the example.

``` { .python }
def left_sidebar_function(request,*args,**kwargs):
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

#### LEFT_SIDEBAR_FUNCTION

The function to be called to render a left sidebar. This function should return
a string containing the HTML for the sidebar. In *TinyWiki* it defaults to the
function ```django_tinywiki.functions.sidebar.render_left_sidebar()```, which
returns the generated html of the function 
```django_tinywiki.functions.get_left_sidebar_data()```.

``` { .python }
def left_sidebar_function(request,*args,**kwargs):
    return """
    <div class="left-sidebar-section">
        <div class="left-sidebar-section-title>Section 1</div>
        <div class="left-sidebar-item>
            <a href="https://www.google.com">Link 1</a>
        </div>
    </div>"""

LEFT_SIDEBAR_FUNCTION = "path.to.left_sidebar_function"
```

#### TINYWIKI_RIGHT_SIDEBAR_FUNCTION

This setting should point to a right sidebar function. The function should
return a list of sidebar items.

``` { .python }
def tinywiki_right_sidebar_function(request,*args,**kwargs):
    right_sidebar_items = [
        '<div class="right-sidebar-item">Sidebar Item 1.</div>',
        '<div class="right-sidebar-item">Sidebar Item 2</div>'
    ]
    return right_sidebar_items

TINYWIKI_RIGHT_SIDEBAR_FUNCTION = "path.to.tinywiki_right_sidebar_function"
```
#### RIGHT_SIDEBAR_FUNCTION

This sets the right sidebar function to use. The function should return
the right sidebar as a HTML-string.

``` { .python }

def right_sidebar_function(request,*args,**kwargs):
    ret = """
        <div class="right-sidebar-item">
            <img src="https://example.org/path/to/image1.png" />
        </div>
        <div class="right-sidebar-item">
            <img src="https://example.org/path/to/image2.jpg" /> 
        </div>"""

    return ret

RIGHT_SIDEBAR_FUNCTION = "path.to.right_sidebar_function"
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

This should be a django-URL-template string pointing to the view that creates a
new TinyWiki page with a given slug. The second argument named **page** of the
view should accept the page slug.

The view should look like ```def wiki_page_create_view(request,page)```.

``` { .python }
TINYWIKI_PAGE_CREATE_URL_TEMPLATE = "tinywiki:page-create"
```

#### TINYWIKI_PAGE_NEW_URL

This setting sepcifies the URL to use for creating new wiki page. The view
should not expect any additional arguments next to the **request**.

``` { .python }
TINYWIKI_PAGE_NEW_URL = reverse_lazy("tinywiki:page-new")
```

#### TINYWIKI_PAGE_DELETE_URL_TEMPLATE

This setting sets the django-url-template of the delete-view for 
*TinyWiki*-pages. The view should accept the page-slug named **page** as second
argument.

```  { .python }
TINYWIKI_PAGE_NEW_URL = "tinywiki:page-delete"
```

#### TINYWIKI_PAGE_OVERVIEW_URL

Set this setting to the URL of the page overview view, if you are implementing
your own.

``` { .python }
TINYWIKI_PAGE_OVERVIEW_URL = reverse_lazy("tinywiki:page-overview")
```

### Project URLs

#### TINYWIKI_LOGIN_URL

This is the login url of the wiki. and is set to 
```reverse_lazy("tinywiki:auth-login")``` if TinyWiki is the main application,
else it is set to the setting *LOGIN_URL*.

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

This setting defines the *Sign Up*-URL of the site. If TinyWiki is the main
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

This settings-variable sets the HTML-template file for the page-create view.

``` { .python}
TINYWIKI_PAGE_CREATE_TEMPLATE = "djnago_tinywiki/wiki/create.html"
```

#### TINYWIKI_PAGE_NEW_TEMPLATE

Set this variable to the page new template. Per default it sets to the variable
```TINYWIKI_PAGE_CREATE_TEMPLATE```.

``` { .python }
TINYWIKI_PAGE_NEW_TEMPLATE = "path/to/new.html"
```

#### TINYWIKI_PAGE_DELETE_TEMPLATE

This variable sets the HTML-template of the page-delete view. The 
*TinyWiki*-view confirms the deletion of the page and if it is 
confirmed, deletes the corresponding page.

``` { .python }
TINYWIKI_PAGE_DELETE_TEMPLATE = "django_tinywiki/wiki/delete.html"
```

#### TINYWIKI_PAGE_DELETE_DONE_TEMPLATE

This variable sets the template for the delete-done page. This page
is only called, if the deletion of the page is confirmed.

``` { .python }
TINYWIKI_PAGE_DELETE_DONE_TEMPLATE = "django_tinywiki/wiki/delete-done.html"
```

#### TINYWIKI_PAGE_OVERVIEW_TEMPLATE

Set this setting to your own template if you want to show your customized
page-overview page.

``` { .python }
TINYWIKI_PAGE_OVERVIEW_TEMPLATE = "django_tinywiki/wiki/ovierview.html"
```

### Application Templates

#### TINYWIKI_LOGIN_TEMPLATE

The template to use for the login view, when running *TinyWiki* in 
standalone-mode.

**Note: This setting is only useful when using *django-tinywiki*'s login view.**

``` { .python }
TINYWIKI_LOGIN_TEMPLATE = "django_tinywiki/auth/login.html"
```

#### TINYWIKI_SIGNUP_TEMPLATE

This setting sets the HTML-template to use for Sign Up when using 
*TinyWiki* in standalone mode.

**Note: This setting is only useful when using *django-tinywiki*'s signup view.**

``` { .python }
TINYWIKI_SIGNUP_TEMPLATE = "django_tinywiki/auth/signup.html"
```

#### TINYWIKI_SIGNUP_SUCCESS_TEMPLATE

The HTML-template to display when the signup on *TinyWiki* was successful.

**Note: This setting is only useful when using *django-tinywiki*'s signup view.**

``` { .python }
TINYWIKI_SIGNUP_SUCCESS_TEMPLATE = "django_tinywiki/auth/signup-success.html"
```

## Auth settings

### User settings

#### TINYWIKI_USER

This are the userdata used to assign the TinyWiki builtin pages to.
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

#### TINYWIKI_DEFAULT_GROUPS

The groups the user is to be added to on creation. This setting
is a list of group names.

``` { .python }
TINYWIKI_DEFAULT_GROUPS = ['tinywiki-user',]
```

### Groups

#### TINYWIKI_GROUP_ADMIN

The group to use for *TinyWiki* admins. Admins can create,delete,edit 
every wiki-page and set the user of every *TinyWiki* page.

``` { .python }
TINYWIKI_GROUP_ADMIN = "tinywiki-admin"
```

#### TINYWIKI_GROUP_AUTHOR

The author group allows *TinyWiki*-authors to create and edit wiki-pages.

``` { .python }
TINYWIKI_GROUP_AUTHOR = "tinywiki-author"
```

#### TINYWIKI_GROUP_USER

The user group lets you edit the wiki-pages that belong to you. Users cannot
create pages.

``` { .python }
TINYWIKI_GROUP_USER = "tinywiki-user"
```

### Permissions

#### TINYWIKI_PERM_ADMIN

This permission gives you you administrative rights for *TinyWiki*.

``` { .python }
TINYWIKI_PERM_ADMIN = "tinywiki-admin"
```

#### TINYWIKI_PERM_CREATE_PAGE

This permission allows users to create new *TinyWiki*-pages.

``` { .python }
TINYWIKI_PREM_CREATE_PAGE = "tinywiki-create-page"
```

#### TINYWIKI_PERM_DELETE_PAGE

This permission allows users to delete *TinyWiki*-pages.

``` { .python }
TINYWIKI_PERM_DELETE_PAGE = "tinywiki-delete-page"
```

#### TINYWIKI_PERM_EDIT_PAGE

This permission allows users to edit *TinyWiki*-pages. The page does not
need to belong to the user with this permission.

``` { .python }
TINYWIKI_PERM_EDIT_PAGE = "tinywiki-edit-page"
```

#### TINYWIKI_PERM_EDIT_USER_PAGE

This permission allows users to edit *TinyWiki*-pages that belong to the user
with this permission.

``` { .python }
TINYWIKI_PERM_EDIT_USER_PAGE = "tinywiki-edit-user-page"
```

#### TINYWIKI_USERPERM_ADMIN

This is the read-only permission for *TinyWiki* admins. It is used for
checking user permissions.

``` { .python }
TINYIWKI_USERPERM_ADMIN = ".".join((TINYWIKI_APP,TINYWIKI_PERM_ADMIN))
```

#### TINYWIKI_USERPERM_CREATE_PAGE

This is the read-only permission used by *TinyWiki* for looking up the user
permission for creating wiki-pages.

``` { .python }
TINYWIKI_USERPERM_CREATE_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_CREATE_PAGE))
```

#### TINYWIKI_USERPERM_DELETE_PAGE

This readonly setting defines the permission used by *TinyWiki* for looking up
the user permission for deleting pages.

``` { .python }
TINYWIKI_USERPERM_DELETE_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_DELETE_PAGE))
```

#### TINYWIKI_USERPERM_EDIT_PAGE

This is the readonly permission used by *TinyWiki* to look up the user permission for 
editing wiki-pages.

``` { .python }
TINYWIKI_USERPERM_EDIT_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_EDIT_PAGE))
```

#### TINYWIKI_USERPERM_EDIT_USER_PAGE

This setting is read only. It is used by *TinyWiki* to look up the user permission
for editing pages that belong to the user, for whom the permission is looked up.

```
TINYWIKI_USERPERM_EDIT_USER_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_EDIT_USER_PAGE))
```