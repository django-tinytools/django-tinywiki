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
