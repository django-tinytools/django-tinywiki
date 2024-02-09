from setuptools import setup,find_packages

setup(
    name="django-tinywiki",
    description="A simple wiki app for the django framework",
    version="0.0.1",
    author="Christian Moser",
    author_email="christian@cmoser.eu",
    install_requires=[
        "django >= 4.2",
	    "django-extras",
	    "pillow >=10.2",
	    "markdown",
    ],
    packages=find_packages(
        include=["django_tinywiki*"],
        exclude=["tinywiki","media","locale"]
    ),
    include_package_data=True,
    package_data={
        'django_tinywiki.locale.de.LC_MESSAGES':["*.mo",],
        'django_tinywiki.builtin_wiki_pages':["*.md","*.jpg","*.png"],
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