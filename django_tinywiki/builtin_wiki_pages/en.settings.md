# TinyWiki Settings

## Table of Contents

[TOC]

## Generic Settings

### TINYWIKI_VERSION

This is a read only settings giving the current version of *django-tinywiki*.

### TINYWIKI_TITLE

The title diplayed in the header bar. Set this to your Wiki/Site name when
using the tinywiki base html template.

``` { .python }
TINYWIKI_TITLE = "TinyWiki"
```

### TINYWIKI_STYLE

``` { .python }
TINYWIKI_STYLE = "default"
```
### TINYWIKI_CSS

``` { .python }
TINYWIKI_CSS = "{url}django_tinywiki/styles/{style}.css".format(
    url=STATIC_URL,
    style=TINYWIKI_STYLE)
```
### TINYWIKI_CODEHILITE_STYLE

``` { .python }
TINYWIKI_CODEHILITE_STYLE = "github-dark"
```

### TINYWIKI_CODEFHILITE_CSS

``` { .python }
TINYWIKI_CODEHILITE_CSS = "{url}django_tinywiki/styles/codehilite/{style}.css".format(
    url=django_settings.STATIC_URL,
    style=TINYWIKI_CODEHILITE_STYLE)
```

### TINYWIKI_MARKDOWN_EXTENSIONS

### TINYWIKI_CONTEXT_CALLBACK

### TINYWIKI_DEFAULT_LANGUAGE

``` { .python }
TINYWIKI_DEFAULT_LANGUAGE = "en"
```


## URL Settings

### TINYWIKI_INDEX

Then index page of TinyWiki. This should be an url pointing to the index
page of *django_tinywiki*.

``` { .python }
 from django.urls import reverse_lazy

 TINYWIKI_INDEX = reverse_lazy("tinywiki:index")
```

### TINYWIKI_HOME_URL

The URL of the homepage of the Site. (This setting is currently unused, but
planned to be used in the future!)

``` { .python }
TINYWIKI_INDEX = "/"
```

### TINYWIKI_PAGE_VIEW_URL_TEMPLATE

If you want to use your own view for rendering *TinyWiki*-pages you can set
this setting to an appropriate value. The set url template is looked up by 
```reverse(TINYWIKI_PAGE_VIEW_URL_TEMPLATE,kwargs={"page":"slug-for-page"})```.

``` { .python }
TINYWIKI_PAGE_VIEW_URL_TEMPLATE = "tinywiki:page"
```
### TINYWIKI_PAGE_EDIT_URL_TEMPLATE

If you are using your own view for editing wiki-pages, set this vairable to
the view you are using.

``` { .python }
TINYWIKI_PAGE_EDIT_URL_TEMPLATE = "tinywiki:page-edit"

```
### TINYWIKI_PAGE_CREATE_URL_TEMPLATE

### TINYWIKI_PAGE_NEW_URL_TEMPLATE

### TINYWIKI_PAGE_DELETE_URL_TEMPLATE

### TINYWIKI_PAGE_OVERVIEW_URL


## Template Settings

### TINYWIKI_BASE_TEMPLATE

This setting defines the base template to be extended by *TinyWiki*.
You can set write your own template and override the default page
layout of *TinyWiki*.

``` { .python }
TINYWIKI_BASE_TEMPLATE = "django_tinywiki/base.html"
```

### TINYWIKI_PAGE_VIEW_TEMPLATE

You can define yourself how Wiki-Pages are displayed by using this setting.
The ```content``` context variable contains the rendered markdown for the
page.

``` { .python }
TINYWIKI_PAGE_VIEW_TEMPLATE = "django_tinywiki/wiki/page.html"
```

### TINYWIKI_PAGE_EDIT_TEMPLATE

Set this variable to your template file, if you want to use your own
template for the edit page.

``` { .python }
TINYWIKI_PAGE_EDIT_TEMPLATE = "django_tinywiki/wiki/edit.html"
```

### TINYWIKI_PAGE_CREATE_TEMPLATE

### TINYWIKI_PAGE_NEW_TEMPLATE

### TINYWIKI_PAGE_DELETE_TEMPLATE

### TINYWIKI_PAGE_DELETE_DONE_TEMPLATE

### TINYWIKI_PAGE_OVERVIEW_TEMPLATE

