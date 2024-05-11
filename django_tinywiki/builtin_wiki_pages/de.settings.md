# TinyWiki Einstellungen

## Inhaltsverzeichnis

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

Die Funktion, welche aufgerufen werden soll, um die linke Seitenleiste
darzustellen. Diese Funktion sollte das HTML der linken Seitenleiste 
zurückgeben. *TinyWiki* verwendet die Funktion
```django_tinywiki.functions.sidebar.render_left_sidebar()``` als
Voreinstellung, wleche das generirte HTML der Funktion
```django_tinywiki.functions.get_left_sidebar_data()``` zurückgibt.

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

Diese Einstellung sollte auf eine Rechte-Seitenleiste-Funktion zeigen.
Die Funktion sollte eine Liste von Seitenleistenelementen zurückgeben.

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

Dies setzt die Funktion um die rechte Seitneleiste darzustellen. Diese
Funktion sollte die rechte Seitneleiste als HTML-String zurückgeben.

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

Diese Einstellung definiert die maximale Breite von Bildern, die auf einer
Wiki-Seite dargestellt werden. Größere Bilder werden in der Größe geändert 
um die maxiamle Breite, die hier angegeben wird, zu haben. Dies sollte die
Ladegeschwindigkeit der Seite verbessern, wenn viele grße Bilder auf einer
Seite verwendet werden.


``` { .pyhton }
TINYWIKI_IMAGE_WIKI_WIDTH = 860
```

#### TINYWIKI_IMAGE_PREVIEW_WIDTH

Die maximale Breite von Vorschaubildern. Dies Sollte das Laden von 
Vorschaubildern beschleunigen. Wenn es dir erlaubt ist eine Seite zu
bearbeiten, wird eine *Verknüpfte Bilder* Sketion, mit Vorschaubildern,
am Ende der Seite angezeigt. 

Es ist auch möglich alle verknüpften Bilder mit dem Tag 
```[WIKI-IAMGES]``` im Wiki-Makrdown anzuzeigen. Die dort angezeigten
Bilder müssen nicht zwigend in der Seite bzw. in der Seitenleiste angezeigt
werden.

Dies sollte das Laden der Seite beschleunigen und die zu übertragende
Datenmenge begrenzen.

``` { .pyhton }
TINYWIKI_IMAGE_PREVIEW_WIDTH = 240
```

#### TINYWIKI_IMAGE_SIDEBAR_WIDTH

Dies definiert die maximale Breite von Seitenleistenbildern. Diese
Einstellung macht nur Sinn, wenn man Seitenleistenbilder eingechaltet
hat.

``` { .python }
TINYWIKI_IMAGE_SIDEBAR_WIDTH = 240
```

### Project Settings

#### TINYWIKI_IS_MAIN_APP

Setze diesen Wert auf ```True```, wenn *TinyWiki* im Standalone-Modus
ausgeführt wird. Andernfalls setze diesen Wert auf ```False```

``` { .python }
TINYWIKI_IS_MAIN_APP = False
```

## URL Settings

### Wiki Urls

#### TINYWIKI_INDEX

Das ist die Hauptseite von *TinyWiki*. Diese Konfigurationsvariable sollte
eine URL beinhalten, die auf die Hauptseite von *django_tinywiki* zeigt.

``` { .python }
 from django.urls import reverse_lazy

 TINYWIKI_INDEX = reverse_lazy("tinywiki:index")
```

#### TINYWIKI_HOME_URL

Das ist die URL der Hauptseite der Site. (Diese Einstellung ist zur Zeit
ungenutzt. Die Nutzung ist aber geplant.)

``` { .python }
TINYWIKI_INDEX = "/"
```

#### TINYWIKI_PAGE_VIEW_URL_TEMPLATE

Wenn du deinen eigenen View zum anzeigen von *TinyWiki*-Seiten verwenden
möchtest, kannst du diese Einstellung auf einen dementsprechenden Wert
setzen. Das URL-Template wird durch 
```reverse(TINYWIKI_PAGE_VIEW_URL_TEMPLATE,kwargs={"page":"slug-for-page"})```
aufgelöst.


``` { .python }
TINYWIKI_PAGE_VIEW_URL_TEMPLATE = "tinywiki:page"
```
#### TINYWIKI_PAGE_EDIT_URL_TEMPLATE

Wenn du deinen eigenen View zum Editieren von Wiki-Seiten verwenden möchtest,
setze diesen Wert auf eine *Django-URL* die auf den View zeigt, den du
verwenden möchtest.

``` { .python }
TINYWIKI_PAGE_EDIT_URL_TEMPLATE = "tinywiki:page-edit"
```

Der View sollte wie folgt aussehen:
```def tinywiki_page_edit_view(request,page)```

#### TINYWIKI_PAGE_CREATE_URL_TEMPLATE

Dies sollte ein *django-URL-template* string ein, der auf den View zeigt,
welcher verantwortlich dafür ist, eine Wiki-Seite mit angegebenen *slug* zu
erstellen. Das zweite Argument **page** des Views sollte den Slug der Seite
akzeptieren.

Der View sollte wie folgt aussehen: 
```def wiki_page_create_view(request,page)```.

``` { .python }
TINYWIKI_PAGE_CREATE_URL_TEMPLATE = "tinywiki:page-create"
```

#### TINYWIKI_PAGE_NEW_URL

Diese Eintellung spezifizeiert die URL, die zu benutzen ist, um neue 
Wiki-Seiten zu erstellen. Der View sollte keine zusätzlichen Argumente,
neben dem *request*, benötigen.

``` { .python }
TINYWIKI_PAGE_NEW_URL = reverse_lazy("tinywiki:page-new")
```

#### TINYWIKI_PAGE_DELETE_URL_TEMPLATE

Diese Einstellung setzt das *Django-URL-Template* für den View, der für
das löschen von *TinyWiki*-Seiten verantwortlich ist. Der View sollte
das Seiten-Slug, mit dem Namen **page** als zweites Argument akzeptieren.

```  { .python }
TINYWIKI_PAGE_NEW_URL = "tinywiki:page-delete"
```

#### TINYWIKI_PAGE_OVERVIEW_URL

Wenn du deine eigene Seitneübersicht erstellen willst, setze die 
URL des Übersichtsviews in dieser Einstellung.

``` { .python }
TINYWIKI_PAGE_OVERVIEW_URL = reverse_lazy("tinywiki:page-overview")
```

### Project URLs

#### TINYWIKI_LOGIN_URL

Das ist die Login URL de Wiki und wird voreingestellt auf 
```reverse_lazy("tinywiki:auth-login")```, wenn TinyWiki die Hauptapplikation
ist. Andernfalls wird sie auf die Variable *LOGIN_URL* gesetzt.

``` { .python }
TINYWIKI_LOGIN_URL = "/login/"
```

#### TINYWIKI_LOGOUT_URL

Die Einstellung setzt die Logout URL der Site. Wenn TinyWiki die 
Hauptapplikation der Site ist, wird sie voreingestellt auf 
```reverse_lazy("tinywiki:auth-logout")``` andernfalls wird der Wert der 
Variablen *LOGOUT_URL* als Voreinstellung genutzt.

``` { .python }
TINYWIKI_LOGOUT_URL = "/logout/"
```

#### TINYWIKI_SIGNUP_URL

Diese Einstellung definiert die *Sing Up*-URL der Site. Wenn TinyWiki die
Hauptapllikation ist, ist der Standardwert 
```reverse_lazy("tinywiki:auth-signup")```, andernfalls wird sie auf den Wert 
der Einstelungsvariable *SIGNUP_URL* gesetzt.

``` { .python }
TINYWIKI_SIGNUP_URL = "/singup/"
```

## Template Settings

### Wiki Templates

#### TINYWIKI_BASE_TEMPLATE

Diese Einstellung definert die Basis Vorlage, die von 
*TinyWiki*-Seiten erwetiert wird. Sie können ihre eigene Vorlage
schreiben und damit das Voreingestellte Seitenlayout von 
*TinyWiki* überschreiben.

``` { .python }
TINYWIKI_BASE_TEMPLATE = "django_tinywiki/base.html"
```

#### TINYWIKI_PAGE_VIEW_TEMPLATE

Sie können definieren, wie Wiki-Seiten dargestellt werden, in dem Sie diese
Einstellung nutzen. Die ```content``` Kontextvariable enthält den gerenderten
Moarkdown für die Seite.

``` { .python }
TINYWIKI_PAGE_VIEW_TEMPLATE = "django_tinywiki/wiki/page.html"
```

#### TINYWIKI_PAGE_EDIT_TEMPLATE

Setzen Sie diese Variable auf ihre Vorlage, wenn Sie ihre eigene Vorlage
zum Bearbeiten von Wiki-Seiten benutzen wollen.

``` { .python }
TINYWIKI_PAGE_EDIT_TEMPLATE = "django_tinywiki/wiki/edit.html"
```

#### TINYWIKI_PAGE_CREATE_TEMPLATE

Diese Einstellungsvariable setzt die HTML-Vorlage, um neue Wiki-Seiten zu
erstellen.

``` { .python}
TINYWIKI_PAGE_CREATE_TEMPLATE = "djnago_tinywiki/wiki/create.html"
```

#### TINYWIKI_PAGE_NEW_TEMPLATE

Setzen sie diese Variable um neue Seiten zu erstellen. Die Voreinstellung 
setzt sie auf die Variable ```TINYWIKI_PAGE_CREATE_TEMPLATE```.

``` { .python }
TINYWIKI_PAGE_NEW_TEMPLATE = "path/to/new.html"
```

#### TINYWIKI_PAGE_DELETE_TEMPLATE

Diese Vairable setzt die HTML-Vorlage des Seite-löschen Views. Dieser 
*TinyWiki*-View bestätigt das löschen der Seite und falls dies bestätigt
wird, wird die entsprechende Seite gelöscht.

``` { .python }
TINYWIKI_PAGE_DELETE_TEMPLATE = "django_tinywiki/wiki/delete.html"
```

#### TINYWIKI_PAGE_DELETE_DONE_TEMPLATE

Diese Vairable setzt das template für die Löschen durchgeführt Seite.
Diese Seite wird nur aufgerufen, wenn das Löschen der entsprechenden 
Wiki-Seite bstätigt wurde.

``` { .python }
TINYWIKI_PAGE_DELETE_DONE_TEMPLATE = "django_tinywiki/wiki/delete-done.html"
```

#### TINYWIKI_PAGE_OVERVIEW_TEMPLATE

Setze diese Variable, wenn du deine eigene angepasste Seitenübersicht anzeigen
willst.

``` { .python }
TINYWIKI_PAGE_OVERVIEW_TEMPLATE = "django_tinywiki/wiki/ovierview.html"
```

### Application Templates

#### TINYWIKI_LOGIN_TEMPLATE

Die Vorlage, die zu nutzen ist, wenn *TinyWiki* in Standalone-Modus
ausgeführt wird.

**Anmerkung: Diese Einstellung ist nur sinnvoll, wenn man *django-tinywiki*s Login Ansicht verwendet.**

``` { .python }
TINYWIKI_LOGIN_TEMPLATE = "django_tinywiki/auth/login.html"
```

#### TINYWIKI_SIGNUP_TEMPLATE

Diese Einstellung stzt das HTML-Template, welches von *TinyWiki* für das
Registrieren neuer Nutzer, verwendet wird, wenn *TinyWiki* im 
Standalone-Modus ausgeführt wird.

**Anmerkung: Diese Einstellung ist nur sinnvoll, wenn man *django-tinywiki*s Signup Ansicht verwendet.**

``` { .python }
TINYWIKI_SIGNUP_TEMPLATE = "django_tinywiki/auth/signup.html"
```

#### TINYWIKI_SIGNUP_SUCCESS_TEMPLATE

Das ist die HTML-Vorlage, die anzuzeigen ist, 
The HTML-template to display when the signup on *TinyWiki* was successful.

**Anmerkung: Diese Einstellung ist nur sinnvoll, wenn man *django-tinywiki*s Signup Ansicht verwendet.**

``` { .python }
TINYWIKI_SIGNUP_SUCCESS_TEMPLATE = "django_tinywiki/auth/signup-success.html"
```

## Auth settings

### User settings

#### TINYWIKI_USER

Das sind die Nutzerdaten, die bneutzt werden, um den Nutzer zu erstellen, der 
die eingabuten *TinyWiki* Seiten erstellt. Erstelle diese Variable als *dict*,
welches die Nutzerdaten als *kwargs*, zum Erstellen des Nutzers mittels
*AUTH_USER_MODEL*, enthält.

``` { .python }
TINYWIKI_USER = {
    'username':'TinyWikiTeam',
    'email': 'tinywiki@cmoser.eu',
    'first_name':'TinyWiki',
    'last_name':'Team',
}
```

#### TINYWIKI_DEFAULT_GROUPS

Diese Variable enthält die voringestellten Gruppen, die zur Erstellung
eines Wiki-Nutzers notwendig sind. Diese Einstellung beinhaltet eine Liste
von Gruppennamen.

``` { .python }
TINYWIKI_DEFAULT_GROUPS = ['tinywiki-user',]
```

### Groups

#### TINYWIKI_GROUP_ADMIN

Die Gruppe, die für *TinyWiki*-Administratoren zu nutzen ist. Administratoren
können alle Seiten erstellen,löschen,editieren und den Nutzer jeder 
*TinyWwiki*-Seite ändern.

``` { .python }
TINYWIKI_GROUP_ADMIN = "tinywiki-admin"
```

#### TINYWIKI_GROUP_AUTHOR

Die Gruppe, die für *TinyWiki*-Autoren zu verwenden ist. Autoren können 
Wiki-Seiten erstellen und editieren.

``` { .python }
TINYWIKI_GROUP_AUTHOR = "tinywiki-author"
```

#### TINYWIKI_GROUP_USER

Die Gruppe für *TinyWiki* Nutzer. Nutzer können Seiten, die ihnen gehören,
editieren. Nutzer können keine eigenen Seiten erstellen.

``` { .python }
TINYWIKI_GROUP_USER = "tinywiki-user"
```

### Permissions

#### TINYWIKI_PERM_ADMIN

Diese Berechtigung gibt ihnen administrative Rechte für *TinyWiki*.

``` { .python }
TINYWIKI_PERM_ADMIN = "tinywiki-admin"
```

#### TINYWIKI_PERM_CREATE_PAGE

Diese Berechtigung erlaubt Nutzern das Erstellen von *TinyWiki*-Seiten.

``` { .python }
TINYWIKI_PREM_CREATE_PAGE = "tinywiki-create-page"
```

#### TINYWIKI_PERM_DELETE_PAGE

Diese Berechtigung erlaubt Nutzern das löschen von *TinyWiki* Seiten

``` { .python }
TINYWIKI_PERM_DELETE_PAGE = "tinywiki-delete-page"
```

#### TINYWIKI_PERM_EDIT_PAGE

Diese Berechtigung erlaubt Nutzern das editieren von *TinyWiki* Seiten. Die
zu editierenden Setien müssen nicht dem Nutzer mit der Berechtigung gehören.

``` { .python }
TINYWIKI_PERM_EDIT_PAGE = "tinywiki-edit-page"
```

#### TINYWIKI_PERM_EDIT_USER_PAGE

Diese Berechtigung erlaubt Nutzern das Editieren der eigenen Seiten. Wenn
diese Erlaubnis entzogen wird, können Nutzer die Seiten, die ihnen gehören
nicht mehr verändern.

``` { .python }
TINYWIKI_PERM_EDIT_USER_PAGE = "tinywiki-edit-user-page"
```

#### TINYWIKI_USERPERM_ADMIN

Das ist die Berechtigung für *TinyWiki*-Admins. Diese Berechtigung
wird nur zum Überprüfen der Nutzerberechtigung gebraucht und kann nur
gelesen werden. 

``` { .python }
TINYIWKI_USERPERM_ADMIN = ".".join((TINYWIKI_APP,TINYWIKI_PERM_ADMIN))
```

#### TINYWIKI_USERPERM_CREATE_PAGE

Diese Berechtigung wird nur zum Überprüfen der Rechte zum Erstellen von
Wiki-Seiten benötigt. Diese Einstellung kann nur gelesen werden.

``` { .python }
TINYWIKI_USERPERM_CREATE_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_CREATE_PAGE))
```

#### TINYWIKI_USERPERM_DELETE_PAGE

Diese Berechtigung wird nur zum Überprüfen der Rechte zum Wiki-Seiten-Löschen
herangezogen. Diese Einstellung kann nur gelesen werden.

``` { .python }
TINYWIKI_USERPERM_DELETE_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_DELETE_PAGE))
```

#### TINYWIKI_USERPERM_EDIT_PAGE

Dies ist die Nutzerberechtigung, die zur Überprüfung der Rechte zum Bearbeiten
von Wiki-Seiten benötigt wird. Diese Einstellung kann nur gelesen werden.

``` { .python }
TINYWIKI_USERPERM_EDIT_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_EDIT_PAGE))
```

#### TINYWIKI_USERPERM_EDIT_USER_PAGE

Diese Nutzerberechtigung kann nur gelesen werden. Sie wird beötigt umd die Rechte
zum Editieren der Seiten, die dem entsprechenden Nutzer göhren, zu überprüfen.

```
TINYWIKI_USERPERM_EDIT_USER_PAGE = ".".join((TINYWIKI_APP,TINYWIKI_PERM_EDIT_USER_PAGE))
```