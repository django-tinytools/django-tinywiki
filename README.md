# Django TinyWiki

*django-tinywiki* is a small minimalistic Wiki for the Django-framework, that
can be loaded as an django app, to provide a simple Wiki for your projects.

*TinyWiki* can also be run as a standalone app.

## Installing

### Installing as an app

*TinyWiki* can be installed using PyPi.

``` { .sh }
pip install django-tinywiki
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

# install the reuirements
pip install -r requirements.txt
```

You can use the *manage* script, which was written for */bin/sh* to execute
the *manage.py* file. The script autmatically loads the python virtual
environment if it is installed in *venv* or *python-venv* in the project
directory or in the parent darectory of the project.
