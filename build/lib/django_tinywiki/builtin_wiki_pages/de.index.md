# Willkommen bei TinyWiki

## Inhaltsverzeichnis

[TOC]

## Info

*django-tinywiki* ist eine kleine, minimalistische Wiki-App für das
Django-Framework. Es lässt sich sowohl als App in ein größeres Projekt
einbinden als auch standalone betreiben. Der Mangel an einer solchen App
hat zu der Entwicklung von TinyWiki geführt.

TinyWiki soll es Django-Entwicklern ermöglichen, einen einfachen Wiki in
größere Projekte zu integrieren.

## Wiki Texte

Als Auszeichnungssprache für den Wiki-Text wurde, auf Grund der Einfachkeit
der Sparche und Lesbarkeit des Quelltexts, Markdown gewählt. Es werden auch
ein Paar Erweiterungen für die Sprache, wie z.B. *TinyWikiLinks* oder
*Verlinkte Bilder* bereitgestellt. Markdown lässt sich auch mit eigenen
Erweiterungen erweitern. Mehr Informationen wie man eigene Erweiterungen
erstellt gibt es in der Anleitung
[Writing Extensions for Python-Markdown](https://python-markdown.github.io/extensions/api/#writing-extensions-for-python-markdown).

Für einen Überblick über das verwendete Markdonwn kontaktiere die
[[Anleitung zum verwendeten Markdown]](de-tinywiki-markdown).

## Installation

### Download per git

``` {.sh}
$ git clone https://github.com/c9moser/django/django-tinywiki
```

+ **TODO** - Github Repository anlegen  
+ **TODO** - pip installation bereitstellen  
+ **TODO** - setup.py

## TinyWiki testen

Um *django-tinywiki* zu testen, lade es em besten über git herunter. Das 
Git-Repository beinhaltet das komplette Django Projekt. Erstelle danach ein
Python-Venv mit dem Namen *venv* oder *python-venv* direkt im 
Projektverzeichnis. Aktiviere das Venv und installiere im Anschluß die 
benötigten Abhängigkeiten, lege einen Superuser account an und initialisiere
TinyWiki.

``` {.sh}
$ # django-tinywiki per git herunterladen
$ git clone https://github.com/c9moser/django/django-tinywiki.git

$ # ins django-tinywiki Verzeichnis wechseln
$ cd django-tinywiki

$ # Venv initialisieren
$ python -m venv --system-site-packages python-venv

# # Venv aktivieren
$ . python-venv/bin/activate

$ # Abhängigkeiten installieren
$ pip install -r requirements.txt

$ # Superuser anlegen
$ ./manage createsuperuser --email email@example.com --username nutzername

$ # TinyWiki initialisieren (TODO)
$ ./manage runscript initapp
```

Danach kann der Wiki ausgeführt werden.

``` {.sh}
./manage runserver
```

Es emfielt sich unter Windows [MSYS2](https://www.msys2.org/) zu verwenden, 
da das *manage* script für *sh* geschrieben wurde.