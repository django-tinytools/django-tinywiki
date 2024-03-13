# Django TinyWiki

*django-tinywiki* is a small minimalistic Wiki for the Django-framework, that
can be loaded as an django app, to provide a simple Wiki for your projects.

*TinyWiki* can also be run as a standalone app.

## Installing

### Installing as an App

#### PyPi Install
*TinyWiki* can be installed using PyPi.

``` { .sh }
pip install django-tinywiki
```

#### Git install

To install clone the repostiroy from git, cd to the downloaded repositroy
and install it with pip.

``` { .sh }
# Fetch the repository
git clone https://github.com/c9moser/django-tinywiki.git

# cd to the project root
cd django-tinywiki

# install it with pip
python -m pip install .
```

#### Required Configuration

To be able to initialize *django-tinywiki*, you need to have 
*django-extensions* enabled in your *settings.py* next to 
*django-tinywiki*.

``` { python }
INSTALLED_APPS = [
    ...
    'django_extensions',
    'django_tinywiki',
]
```

### Installing as Standalone App

To Install *TinyWiki* as a standlone app, the easiest way to do it, is using Git.

``` { .sh }
git clone https://github.com/c9moser/django-tinywiki.git
```

Then create a virtual environment and install all requirements.

``` { .sh }
# cd to the django-tinywiki directory
cd django-tinywiki

# create a virtual environment and activate it
python -m venv --system-site-packages python-venv
. python-venv/bin/activate

# install the requirements
pip install -r requirements.txt
```

You can use the *manage* script, which was written for */bin/sh* to execute
the *manage.py* file. The script autmatically loads the python virtual
environment if it is installed in *venv* or *python-venv* in the project
directory or in the parent directory of the project.

#### Overwriting settings.py

To overwrite the settings in *settings.py*, create a file named 
**project_settings.py** in the tinywiki directory. The settings in that file
are imported, if **project_settings.py** exists, at the end of *settings.py*.

### Initializing django-tinywiki

Before you can start using that app, you have to *migrate* the database, create
a superuser and initialize *django-tinywiki*. To initialize *django-tinywiki*
run the script *initapp*. This initializes the wiki and creates the default pages.

```
# migrate the database
python manage.py migrate

# create a superuser
python manage.py createsuperuser --username USERNAME --email email@example.com

# initialize django-tinywiki
python manage.py runscript initapp
```
