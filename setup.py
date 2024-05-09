from setuptools import setup,find_packages

setup(
    name="django-tinywiki",
    description="A simple wiki app for the django framework",
    version="0.0.4",
    author="Christian Moser",
    author_email="christian@cmoser.eu",
    install_requires=[
        "django >= 4.2",
	    "django-extras",
	    "pillow >=10.2",
	    "markdown",
        "pygments",
    ],
    packages=find_packages(
        include=["django_tinywiki*"],
        exclude=["tinywiki","media","locale"]
    ),
    include_package_data=True,
    package_data={
        'django_tinywiki': [
            'builtin_wiki_pages/*',
            'static/django_tinywiki/images/*.png',
            'static/django_tinywiki/images/*.jpg',
            'static/django_tinywiki/videos/*.avi',
            'static/django_tiynwiki/videos/*.mp4',
            'static/django_tinywiki/styles/*.css',
            'static/django_tinywiki/styles/codehilite/*.css',
            'templates/django_tinywiki/*.html',
            'templates/django_tinywiki/auth/*.html',
            'templates/django_tinywiki/manage/*.html',
            'templates/django_tinywiki/wiki/*.html',
            'locale/*/LC_MESSAGES/*.po',
            'locale/*/LC_MESSAGES/*.mo',
        ]
    },
    url="https://github.com/c9moser/django-tinywiki",
    license="BSD-3-Clause",
    license_files=["LICENSE",],
    zip_safe=False,
    python_requires=">= 3.9",
    project_urls={
        'Homepage':"https://github.com/c9moser/django-tinywiki",
        'Issues': "https://www.github.com/c9moser/django-tinywiki/issues",
    }
)
