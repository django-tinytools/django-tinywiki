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

**Alle Versionen vor 0.1 sollten als instabil angesehen werden!**

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

``` { .sh use_pygments=true }
python -m pip install django-tinywiki
```

Nach dem Installieren aktiviere *django-tinywiki* in der *setup.py*
des Projekts.

``` { .python }
INSTALLED_APPS = [
    ...
    "django_tinywiki",
    ...
]
```

Danach Initialisiere *django-tinywiki* durch das ausführen des 
*initapp*-Scripts.

``` { .sh }
python manage.py runscript initapp
```

### Installation per git

``` { .sh }
git clone https://github.com/c9moser/django-tinywiki.git
cd django-tinywiki
pip install .
```

### TinyWiki testen oder als Standalone

Um *django-tinywiki* zu testen, lade es em besten über git herunter. Das 
Git-Repository beinhaltet das komplette Django Projekt. 

Erstelle danach ein *Python Virtual Environment* mit dem Namen *venv* oder 
*python-venv* direkt im Projektverzeichnis oder dem Elternverzeichnis des
Projekts. Das erlaubt die asuführung des *manage* Scripts.

Aktiviere das Venv und installiere im Anschluß die benötigten Abhängigkeiten,
lege einen Superuser account an und initialisiere TinyWiki mit dem 
Django-Script *initapp*.

``` { .sh }
# django-tinywiki per git herunterladen
git clone https://github.com/c9moser/django-tinywiki.git

# ins django-tinywiki Verzeichnis wechseln
cd django-tinywiki

# Venv initialisieren
python -m venv --system-site-packages python-venv

# Venv aktivieren
. python-venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# Superuser anlegen
./manage createsuperuser --email "email@example.com" --username "nutzername"

# TinyWiki initialisieren
./manage runscript initapp
```

Danach kann der Wiki ausgeführt werden.

``` { .sh }
./manage runserver
```

Es emfielt sich unter Windows [MSYS2](https://www.msys2.org/) zu verwenden, 
da das *manage* script für *sh* geschrieben wurde. Andernfalls wirst du
selbst ein Script für *PowerShell* oder die *cmd.exe* schreiben wollen,
um die *manage.py* Datei mit der inkludierten virtuellen Pyton-Umgebung
ausführen zu können.


#### SECRET_KEY

Wenn du nur deinen eigenen *SECRET_KEY* bereitstellen, was empfohlen wird,
willst, erstelle eine Datei mit dem Namen *secret_key.py* und der *SECRET_KEY*
Variablen im *tinywiki* Verzeichnis. Du kannst auch *SECRET_KEY_FALLBACKS* in
diese Datei einfügen.

Inhalt der *secret_key.py*:

``` { .python }
SECRET_KEY = "django-secret-key-with-your-secret"
SECRET_KEY_FALLBACKS = [
    "last-django-secret-key",
    "older-django-secret-key",
]
```

#### Überschreiben der Standardkonfiguration

Um einen oder mehrere Werte der Stnadardeinstellungen zu überschreiben,
erstelle die Datei *project_settings.py* im *tinywiki* Verzeichnis. Diese
Datei sollte alle Konfiurationsvariablen enthalten, die überschreiben werden
sollen. Die Werte dieser Datei werden am Ende der *settings.py* eingebunden
und überschreiben alle vorherigen Werte.

## Einstellungen

Die verfügbaren Einstellungen für *TinyWiki* entnehmen sie der 
[[Anleitung für TinyWiki Einstellungen]](de-tinywiki-settings)
