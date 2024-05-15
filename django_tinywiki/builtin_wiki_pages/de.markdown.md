{% load static %}
# TinyWiki Markdown Syntax

## Inhaltsverzeichnis

[TOC]

## Einleitung

**Markdown** ist eine simple Auszeichnungssprache, die es erlaubt ihren Inhalt
als HTML abzubilden. TinyWiki nutzt Markdown für seine Wikiseiten. Guthub zum
Beispiel nutzt auch Markdown für seien README-Dateien.

Die kurze Anleitung gibt einen Überblick des verwendeten Markdown Syntax und
die verwendeten Markdown Erwetierungen.

## WikiPage als Templates
*TinyWiki*-Seiten werden zuerst von dem Django's Template Prozessor bearbeitet
bevor sie als Markdown bearbeitet werden. Das erlaubt z.B.: das Verlinken auf
statischen Inhalt.

Wie z.B.:

``` { .markdown }
{% templatetag openblock %} load static {% templatetag closeblock %}

![Pfau im Schloss Eggenberg]({% templatetag openblock %} static 'django_tinywiki/images/peacock.jpg' {% templatetag closeblock %})
```

![Pfau im Schloss Eggenberg]({% static 'django_tinywiki/images/peacock.jpg' %})

### Django Template Tags

Um Django's Templatetags auszugeben verwende das Template ```templatetag```.

``` { .markdown }
{% templatetag openblock %} templatetag openblock {% templatetag closeblock %}
```

Template Argumente sind wie folgt:

Argument      |      Tag
------------- | --------------------------------
openblock     | {% templatetag openblock %}
closeblock    | {% templatetag closeblock %}
openvariable  | {% templatetag openvariable %}
closevariable | {% templatetag closevariable %}
openbrace     | {% templatetag openbrace %}
closebrace    | {% templatetag closebrace %}
opencomment   | {% templatetag opencomment %}
closecomment  | {% templatetag closecomment %}

## Überschriften

Um eine Überschrift in Markdown zu erstellen, beginne eine Zeile mit mindestens
einen Rautezeichen ```#``` gefolgt von einem Leerzeichen. Die Anzahl der
Rautezeichen bestimmen die Ebene der Überschrift.

``` { .markdown }
# Überschrift Ebene 1

## Überschrift Ebene 2

### Überschrift Ebene 3

#### Überschrift Ebene 4

##### Überschrift Ebene 5

###### Überschrift Ebene 6
```

### Alternativer Syntax

Um eine Ebene-1 Überschrift zu erzeugen, kann man den Text der Überschrift mit
einem Gleich-Zeichen ```=``` unterstreichen. Für eiene Ebene-2 Überschrift
kann man den Text mit einem Minuszeichen unterstreichen. Es kann jede beliebige
Anzahl an Zeichen zum Unterstreichen verwendet werden, es sollten aber
mindestens drei Zeichen sein.

``` { .markdown }
Überschrift Ebene 1
===================

Überschrift Ebene 2
-------------------
```

## Absätze und Zeilenumbrüche

Um einen Absatz zu erstellen nutze mindestens eine Leerzeile zwischen einer
oder mehereren Zeilen an Text.

Einen Zeilenumbruch erstellt man, in dem man die Zeile mit Text mit zwei oder
mehr Leerzeichen beendet.

### Beispiel

``` { .markdown }
Das ist eine Zeile,
gefolgt von einer Zeile.

Das ist ein neuer Absatz.
Diese Zeile endet mit zwei Leerzeichen.  
Das ist eine neue Zeile.
```

**Die Ausgabe des vorangegangenen Beispiels ist:**

Das ist eine Zeile,
gefolgt von einer Zeile.

Das ist ein neuer Absatz.
Diese Zeile endet mit zwei Leerzeichen.  
Das ist eine neue Zeile.

## Fetter, kursiver und durchgestrichener Text

Um einen Text *kursiv* zu machen, bette den Text zwischen einem Sternzeichen
```*text*``` oder einem Unterstrich ein ```_text_```.

Um einen Text **fett** zu machen, bette den Text zwischen zwei Sternzeichen
```**text**``` oder zwei Unterstrichen ein ```__text__```.

Um einen Text ***fett und kursiv zu machen*** nutze drei Sternzeichen
```***text***```, beziehungsweise drei Unterstriche ```___text___```.

Einen ~~durchgestrichenen Text~~ erzeugt man in dem man ihn zwischen zwei
Tildezeichen einbettet ```~~text~~```.

``` { .markdown }
*kursiv*,
**fett**,
***kursiv und fett***,
**_fett und krusiv_ - nur mehr fett**,
~~durchgestrichen~~
```

**Die Ausgabe des obigen Beispiels ist:**

*kursiv*,
**fett**,
***kursiv und fett***,
**_fett und krusiv_ - nur mehr fett**,
~~durchgestrichen~~

## Copyright usw.

Um ein Copyright Zeichen (C) wird mit ```(C)```, eine registrierte
Handelsmarke (R) mit ```(R)``` und ein Warenzeichen mit (TM) mit
```(TM)``` dargestellt.

``` { .markdown }
(C) 2024 Django(R) TinyWiki(TM)
```

(C) 2024 Django(R) TinyWiki(TM)

**_CopyrightExtension_ ist eine TinyWiki erweiterung und kein Markdown Standard!**

## Zitate

Um ein Zitat hinzuzufügen, beginne einen Absatz mit einem Größerzeichen
```>```.

``` { .markdown }
> Das ist ein Zitat.
> Das Zitat wird fortgesetzt.
```

**Das obige Beispiel wird wi folgt Ausgegeben:**

> Das ist ein Zitat.
> Das Zitat wird fortgesetzt.

### Zitate und Absätze

Um ein, mehrere Absätze umspannended Zitat, zu erzeugen, plaziere bis auf ein
```>``` leere Zeilen als Absatztrenner zwischen den Zitattext.

``` { .markdown }
> Das ist der erste Absatz.
>
> Das ist der Zweite Absatz.
```

**Die Ausgabe des obigen Beispiels:**

> Das ist der erste Absatz.
>
> Das ist der Zweite Absatz.

### Verschachtelte Zitate

Verschachtelte Zitate werden erzeugt, in dem man mehrere Größerzeichen
```>>``` verwendet.

``` { .markdown }
> Das ist ein Zitat.
>
>> Das ist ein verschachteltes Zitat.
```

**Die Ausgabe de Beispiels:**

> Das ist ein Zitat.
>
>> Das ist ein verschachteltes Zitat.

## Listen

Um ungeordnete Listen zu erstellen verwendet man einen Stern ```*```, ein Plus
```+``` oder einen Strich ```-```. Jedes dieser Zeichen führt zu dem selben
Ergebnis. Um eine verschachtelte Liste zu erstellen, rücke das Listenzeichen
mit einem Tabulator oder mit vier Leerzeichen ein.

``` { .markdown }
* Posten 1
* Posten 2
* Posten 3
    * Posten 3.1
```

**Die Ausgabe sieht wie folgt aus:**

* Listenposten 1
* Listenposten 2
* Listenposten 3
    * Listenposten 3.1

Eine geordnete Liste wird erstellt, in dem man eine Zahl mit einem Punkt danach
verwndet ```1. Listenposten```.

``` { .markdown }
1. Listenposten 1
2. Listenposten 2
3. Listenposten 3
    1. Listenposten 3.1
```

**Und die Ausgabe:**

1. Listenposten 1
2. Listenposten 2
3. Listenposten 3
    1. Listenposten 3.1

## Tabellen

Mit *Pipes* ```|``` werden Markdowntabellen erstellt. Jede Spalte wird mit
einem Pipezeichen getrennt. Um Tabellenüberschriften zu erzeugen, 
unterstreiche die Spalte mit einem Strich ```-```.

Hier ein Beispiel:

``` { .markdown }
Spalte 1 | Spalte 2 | Spalte 3
-------- | -------- | --------
    A1   |    B1    |    C1
    A2   |    B2    |    C2
    A3   |    B3    |    C3
```

**Das Beispiel sieht wie folgt aus:**

Spalte 1 | Spalte 2 | Spalte 3
-------- | -------- | --------
    A1   |    B1    |    C1
    A2   |    B2    |    C2
    A3   |    B3    |    C3

## Codeblöcke

Du kannst Codeblöcke erzeugen, in dem du den Quelltext zwischen
drei Backticks ``` ` ``` einbettest. Um einen mehreren Zeilen
umspannenden Codeblock zu erzeugen, beginne und beende einen
Absatz mit drei Backticks.

```` { .markdown }
Text ```Code kommt hier rein``` Text

```
Viele
Zeilen
von
Quelltext
```
````

**Die Ausgabe des obigen Beispiels:**

Text ```Code kommt hier rein``` Text

``` { .markdown }
Viele
Zeilen
von
Quelltext
```

Um eine detaillierterte Anleitung über Codeblöcke zu erhalten, besuche die
[Python markdown fenced code blocks extension documentation](https://python-markdown.github.io/extensions/fenced_code_blocks/).

## Links

Um einen Link den Text hinzuzufügen plaziere den Linktitel zwischen eckige 
Klammern ```[]``` gefolgt von der Linkadresse in runden Klammern ```()```.
Der Link hat das Format ```[Link Titel](url)```.

``` { .markdown }
[Goole Suche](https://www.google.com)
```

**Das ergibt:**

[Goole Suche](https://www.google.com)

### TinyWiki Links

Um TinyWiki-Links bereit zu stellen nutze platziere den Slug der aufzurufenden
Seite ziwschen zwei eckige Klammern ```[[wiki-slug]]```.

Man kann auch einen Link mit alternativen Titel erzeugen, indem man den Titel
ziwschen zwei eckige Klammern, gefolgt von dem Slug in runden Klammern, setzt
```[[Alternativer Titel]](wiki-slug)```.

**_TinyWiki Links_ sind eine TinyWiki Erweiterung!**

``` { .markdown }
* [[de-tinywiki-index]]
* [[link-existiert-nicht]]
* [[Deutsche Django's TinyWiki Hauptseite]](de-tinywiki-index)
* [[Diese Seite existiert nicht]](link-existiert-nicht)
```

**Dieses Beispiel wird wie folgt ausgegeben:**

* [[de-tinywiki-index]]
* [[link-existiert-nicht]]
* [[Deutsche Django's TinyWiki Hauptseite]](de-tinywiki-index)
* [[Diese Seite existiert nicht]](link-existiert-nicht)

### Django Links

Um Django Links zu erzeugen, nutze die ```$[text](app:name)``` notation. 
*app* ist der Applikationsname in der urls-Datei, *name* ist der name der
URL und *text* ist der Linktext, der den Nutzer Angezeigt wird. Der Link
wird mit Hilfe der Funktion ```django.shortcuts.reverse()``` erzeugt.

Wenn du Variablen in der URL brauchst, nutze das 
```$[text](app:name|variable|...)``` Format, bei welchem die variablen mit
einem Pipezeichen ```|``` getrennt werden.

**_Django Links_ sind eine TinyWiki erweiterung und kein Teil des Django-Frameworks!**

Hier ein Beispiel:

``` { .markdown }
* $[Hauptseite](tinywiki:index)
* $[Hauptseite erneut](tinywiki:page|de-tinywiki-index)
```

* $[Hauptseite](tinywiki:index)
* $[Hauptseite erneut](tinywiki:page|de-tinywiki-index)

## Bilder

Bilder einbetten funktioniert mit dem Format ```![alt Text](image-url)```.

Um mit der Wikiseite verlinkte Bilder einzubinden, verwende das Format
```![[image-id]]```. Eingebaute Bilder lassen sich mit dem Format
```![[!eingebaute-bild-id]]``` einbinden. Negative Zahlen für
*eingebaute-bild-id* sind für die TinyWiki internen Seiten reserviert.
Nutze also positive Nummern für deine *eingebaute-bilder-id*s.

``` { .markdown .overflow-auto}
![Picture of hemp](https://de.seedfinder.eu/pics/galerie/Serious_Seeds/AK47/17092099828694083_big.jpg)

![[---1000--]]

![[!-1001]]
```

**Die Ausgabe des Beispiels sieht wie folgt aus:**

![Picture of hemp](https://de.seedfinder.eu/pics/galerie/Serious_Seeds/AK47/17092099828694083_big.jpg)

![[---1000--]]

![[!-1001]]


Um die verknüpften Bilder deiner TinyWiki-Seite anzuzeigen, nutze den Tag
```[WIKI-IMAGES]```. Dieser Tag generiert einen Grid mit den Vorschaubildern
der, mit deiner Seite verknüpften, Bilder.

``` { .markdown }
### Verknüpfte Bilder

[WIKI-IMAGES]
```

**Das ergibt:**

### Verknüpfte Bilder

[WIKI-IMAGES]

## Vidoes einbinden

``` { .markdown }
?[Django tutorial](youtube:rHux0gMZ3Eg)

?[Quallen]({% static 'django_tinywiki/videos/Jellyfish.mp4' %})

?[Quallen mit Breite und Höhe]({% static 'django_tinywiki/videos/Jellyfish.mp4' %}|560,315)
```

?[Django tutorial](youtube:rHux0gMZ3Eg)

?[Quallen]({% static 'django_tinywiki/videos/Jellyfish.mp4' %})

?[Quallen mit Breite und Höhe]({% static 'django_tinywiki/videos/Jellyfish.mp4' %}|560,315)

**Embedding Videos is a TinyWiki extension**

## Ein Inhaltsverzeichnis erstellen

Um ein Inhaltsverzeichnis zu erstellen, verwende den ```[TOC]```-Tag in einem
eigenen Absatz.

```{ .markdown }
...

[TOC]

...
```

...

[TOC]

...
