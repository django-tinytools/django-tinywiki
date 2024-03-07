# Welcome to TinyWiki

## Table of Contents

[TOC]

## Info

*django-tinywiki* is a small, minimalistic Wiki-App for the Django-Frmaework.
It can be used as an app and as a standalone Project. The absence of such an
app has lead to the development of TinyWiki.

TinyWiki shall allow Django-developers to integrate a simple Wiki in larger
Projects.

**All Versions before 0.1 shall be considered unstable!**

## Wiki Texts

As markup-language for Wiki-Texts, because of its readability of the source 
code and its simplicity, *Markdown* was chosen. There are also some extensions
for Markdown provided, like *TinyWikiLinks* or *Linked Images*. There is also
the possibility of extending Markdown with ones own extensions. For more 
information on extending Markdown read the Guide
[Writing Extensions for Python-Markdown](https://python-markdown.github.io/extensions/api/#writing-extensions-for-python-markdown).

An overview of the used Markdown for Wiki-pages can be found in the
[[Guide for used Markdown]](en-tinywiki-markdown).

## Installation

You can install *django-tinywiki* directly from PyPI.

```
python -m pip install django-tinywiki
```

After installing *django-tinywiki* enable it in your project's *settings.py*.

``` { .python }
INSTALLED_APPS = [
    ...
    "django_tinywiki",
    ...
]
```

Then initialize it by running the initapp script:

``` { .sh }
python manage.py runscript initapp
```

### Installation via git

``` { .sh }
$ git clone https://github.com/c9moser/django-tinywiki.git
$ cd django-tinywiki
$ pip install .
```

### Testing TinyWiki or running it standalone

If you want to test *django-tinywiki*, download the git repository.
The Repository conatains the complete django-project.

Create a *Python Virtual Environemnt* with the name *venv* or 
*python-venv* in the project directory or the parent directory of the 
project. This allows the *manage* script to work properly.

After that activate the virtual environment and install the requirements
of the app. They are found in the *requirements.txt*.

Then create a superuser account and initialize TinyWiki by running the
*initapp* script.


``` { .sh }
$ # download the django-tinywiki repository using git
$ git clone https://github.com/c9moser/django-tinywiki.git

$ # Move in the django-tinywiki directory
$ cd django-tinywiki

$ # Python Virtual environment initialisieren
$ python -m venv --system-site-packages python-venv

# # activate the virtual environment
$ . python-venv/bin/activate

$ # Install the reuirements
$ pip install -r requirements.txt

$ # Create a superuser account
$ ./manage createsuperuser --email "email@example.com" --username "username"

$ # Initialize TinyWiki
$ ./manage runscript initapp
```

You can run TinyWiki after the initial setup.

``` { .sh }
./manage runserver
```

For Windows users, it is recomended to use [MSYS2](https://www.msys2.org),
to be able to use the manage script. If not you might want to write your
own script for *PowerShell* or *cmd.exe*.

#### SECRET_KEY

If you just want to provide your own *SECRET_KEY*, which is recommended,
create a file *secret_key.py* in the *tinywiki* directory. You can also
provide the *SECRET_KEY_FALLBACKS* value in *secret_key.py*

Content of the *secret_key.py*

``` { .python }
SECRET_KEY = "django-secret-key-with-your-secret"
SECRET_KEY_FALLBACKS = [
    "last-django-secret-key",
    "older-django-secret-key",
]
```

#### Overwriting default settings

To overwrite one or more of the default settings, provide the file
*project_settings.py* in the *tinywiki* directory. You can place all
of your settings there. They will overwrite the default settings.

## Settings

To view the available settings for *TinyWiki* visit the [[Settings Documentation]](en-tinywiki-settings).

