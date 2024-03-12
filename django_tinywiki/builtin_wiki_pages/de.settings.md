# TinyWiki Einstellungen

## Ihaltsverzeichnis

[TOC]

## Generische Einstellungen

### Version

#### TINYWIKI_VERSION

Diese nur lesen Einstellung enthält die verwendete Version von 
*django-tinywiki* als ein String.

### Package and App

#### TINYWIKI_PACKAGE

Diese nur lesen Einstellung enthält den paketnamen von *Tinywiki*. 
Der Name wird dynamisch, vom Paketverzeichnis, generiert.

#### TINYWIKI_APP

Der nur lesen name der Django Applikation. Derzeit ist es das selbe wie
```TINYWIKI_PACKAGE```

### Applikationseinstellungen

#### TINYWIKI_TITLE

Das ist der Titel, der in der Titelleiste angezeigt wird. Setze diese
Einstellung auf den Namen deines Wikis / deiner Site wenn du das 
tinywiki-base HTML template verwendest.

``` { .python }
TINYWIKI_TITLE = "TinyWiki"
```

#### TINYWIKI_STYLE

Du kannst das den CSS-Stil für *TinyWiki* mit dieser Einstellung auswählen.
Das dzugehörige Stylesheet wird automatisch ausgewählt. 

Um die verfügbaren Stile anzuzeigen führe das *tinywiki_styles* script aus.

``` { .sh }
$ ./manage runscript tinywiki_styles
```

Setze die *TINYWIKI_STYLE* variable auf einen Stilnamen auf einen der 
verfügbaren Stile. (Zur Zeit wird nur der *default* Stil unterstützt.)

``` { .python }
TINYWIKI_STYLE = "default"
```

#### TINYWIKI_CSS

Wenn du dein eigenes CSS-Stylesheet deiner applikation verwenden möchtest
und du den Stil von *django-tinywiki* ignorieren möchtest, gib das zu 
verwendende Stylesheet in der Einsteelung *TINYWIKI_CSS* an.

``` { .python }
TINYWIKI_CSS = "/static/styles/my_style.css"
```
#### TINYWIKI_CODEHILITE_STYLE

Du kannst den *codehilite* Stil auf einen der Unterstützen Stile setzen,
wenn du das Aussehen der Code-Sektionen deiner Wiki-Seiten ändern wills.

``` { .python }
TINYWIKI_CODEHILITE_STYLE = "github-dark"
```

Um alle verfügbaren Stile anzuzeigen, verwende das Script
*tinywiki_codehilite_styles*.

``` { .sh }
$ ./manage runscript tinywiki_codehilite_styles
```

#### TINYWIKI_CODEFHILITE_CSS

Du kannst auch dein eigenes CSS-Stylesheet für die Code-Sektionen in deinen
Wiki-Seiten verwenden, in dem du die ```TINYWIKI_CODEHILITE_CSS``` Variable
auf das einzubindende CSS-Stylesheet setzt.

``` { .python }
TINYWIKI_CODEHILITE_CSS = "/static/styles/my_codehilite_style.css"
```

#### TINYWIKI_MARKDOWN_EXTENSIONS

Du kannst deine eigenen Markdown Erweiterungen für die Verwendung in Wiki-Seiten
importieren, wenn dies benötigt wird. Um dies zu bewerkstelligen gib mit dem 
Konfigurationsparameter ```TINYWIKI_MARKDOWN_EXTENSIONS``` die Liste der 
Markdown-Erweiterungen, die einzubinden sind, an.

Mehr Informationen zu Markdown-Erweitrungen gibt es in dem Dokument
[Makrdown Extensions](https://python-markdown.github.io/extensions/) und in
[writing Markdown Extensions](https://python-markdown.github.io/extensions/api/).

``` { .python }
TINYWIKI_MARKDOWN_EXTENSIONS = [MarkdowExtension1(),"path.to:MarkdownExtension2"]
```

#### TINYWIKI_CONTEXT_CALLBACK

Diese Einstellung definiert die Context-Callback-Funktion, die für *TinyWiki*-
Views verwendet wird an. Eine eigene Context-Funktion kann nützlich sein, wenn
man eigene Templates verwendet und die Context-Variablen erweitert werden sollen.

``` { .python }
def context_function(request):
    context = {
        'context_variable':'value',
    }
    return context

TINYWIKI_CONTEXT_CALLBACK = context_function
```

Du kannst die Context-Funtkion auch als string angeben:

``` { .python }
TINYWIKI_CONTEXT_CALLBACK = "path.to.context_function"
```

#### TINYWIKI_DEFAULT_LANGUAGE

Das ist die voreingestellte Sprache für das erstellen von *TinyWiki*-Seiten.
Die angegebene Sprach-Code muss in der Datenabank existieren, andernfalls wird
**en** als Wert angegeben.

``` { .python }
TINYWIKI_DEFAULT_LANGUAGE = "en"
```

#### TINYWIKI_LEFT_SIDEBAR

Das ist die linke Seitenleiste von *TinyWiki*. Setze diese auf eine Liste von
Seitenleisten-Sektionen-Spezifikatoren. Das Layout dieser Variable wird im 
Beispiel dargestellt.

```TINYWIKI_LEFT_SIDEBAR``` wird für statischen Seitenleisteninhalt verwendet.
Wenn du einen dynamischen Inhalt darstellen willst, verwende die
```TINYWIKI_LEFT_SIDEBAR_FUNCTION``` Variable um eine Funktion aufzurufen, die
dazu verwendet wird, den Inhalt der linken Seitneleiste  für *TinyWiki*-Views
dynamisch zu erstellen.

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

Gib hier eine Funktion an, die aufgerufen wird, um eine dynamische
linke Setienleiste zu erstellen. Die Funktion wird mit einer
```request``` Instanz des auszuführenden Views, aufgerufen.

Diese Funktion sollte eine Liste von 
Seitenleisten-Sektion-Spezifikatoren zurückgeben. Das Layout des
Rückgabewertes wird in dem Beispiel angezeigt.

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

Set this setting to the URL of the page delete view, if you are implementing
your own.

``` { .python }
TINYWIKI_PAGE_OVERVIEW_URL = reverse_lazy("tinywiki:page-overview")
```

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

This variable sets the template for the delete-confirmation page.

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

This setting set the HTML-template to use when using django_tinywiki.

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

This permission allows users to edit *TinyWiki*-pages. The page doeas not
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

This is the read only permission for *TinyWiki* admins. It is used for
checking user permissions.

``` { .python }
TINYIWKI_USERPERM_ADMIN = ".".join((TINYWIKI_APP,TINYWIKI_PERM_ADMIN))
```

#### TINYWIKI_USERPERM_CREATE_PAGE

This is the read only permission used by *TinyWiki* for looking up the user
permission for creating wiki-pages.

``` { .python }
TINYWIKI_USERPERM_CREATE_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_CREATE_PAGE))
```

#### TINYWIKI_USERPERM_DELETE_PAGE

This read only setting defines the permission used by *TinyWiki* for looking up
the user permission for deleting pages.

``` { .python }
TINYWIKI_USERPERM_DELETE_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_DELETE_PAGE))
```

#### TINYWIKI_USERPERM_EDIT_PAGE

This is the read only permission used by *TinyWiki* to look up the user permission for 
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