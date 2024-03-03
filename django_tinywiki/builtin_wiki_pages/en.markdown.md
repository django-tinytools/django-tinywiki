# TinyWiki Markdown Syntax

## Table of Contents

[TOC]

## Introduction

**Markdown** is a simple markup language that allows to render it content in
HTML. TinyWiki uses Markdown for its Wiki-pages. Github for example
uses Markdown too for its README-files.

This short guide gives you an overview of the *Markdown*-syntax.

## WikiPage als Templates

*TinyWiki*-pages are fist processed by Django's template prcessor before the
Markdown is processed. This allows for example emebdding static content.

Wie z.B.:

``` { .markdown }
{% templatetag openblock %} load static {% templatetag closeblock %}

![Pfau im Schloss Eggenberg]({% templatetag openblock %} static 'django_tinywiki/images/peacock.jpg' {% templatetag closeblock %})
```

![Pfau im Schloss Eggenberg]({% static 'django_tinywiki/images/peacock.jpg' %})

Like for example:

``` { .markdown }
{% templatetag openblock %} load static {% templatetag closeblock %}

![Peacock in Eggenberg castle]({% templatetag openblock %} static 'django_tinywiki/images/peacock.jpg' {% templatetag closeblock %})
```

![Peacock in Eggenberg castle]({% static 'django_tinywiki/images/peacock.jpg' %})

### Django Template Tags

To render Django's templatetags use the template ```templatetag```.

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

## Headings

To create a headings in *Markdown*, start the line with atleast one hash sign
```#``` followed by a space. The number of hash signs define the level of the
heading.

``` { .markdown }
# Heading Level 1

## Heading Level 2

### Heading Level 3

#### Heading Level 4

##### Heading Level 5

###### Heading Level 6
```

### Alternate syntax

To create a level 1 heading you can underline the heading text with any number
of equal signs ```=```. For level 2 can be created by underlining the text with
any number dashes ```-```.

``` { .markdown }
Heading Level 1
===============

Heading Level 2
---------------
```

## Paragraphs and Line breaks

To create a paragraph use atleast one empty line between one or more lines of 
text. To create a line break end the line with two or more spaces.

### Expamle
``` { .markdown }
This is a line.
Followed by a line.

This is a new paragraph.
This line ends with two spaces.  
This is a new line.
```

The output of the previous example is:

This is a line.
Followed by a line.

This is a new paragraph.
This line ends with two spaces.  
This is a new line.

## Bold, italic and crossed out text

To make a text *italic* use embed yout text in between one asterisk 
```*text*```.  
To make a text **bold** use two asterisks ```**text**```.  
To make a text ***bold and italic*** use three asterisks 
```***text***```.

To ~~crossed out~~ text is created by encapsulating the text between
two tilde charcaters ```~~text~~```.
``` { .markdown }
*italic*
**bold**
***bold and italic***
~~crossed out~~
```

It renders to:  
*italic*
**bold**
***bold and italic***
~~crossed out~~

## Copyright and such

A copyright sign (C) is created with ```(C)```, a Registered Trademark (R) is
created with ```(R)``` and a Trademark (TM) with ```(TM)```.

``` { .markdown }
(C) 2024 Django(R) TinyWiki(TM)
```

(C) 2024 Django(R) TinyWiki(TM)

## Blockquotes

To add a blockquote, place a ```>``` in front of a paragraph.

``` { .markdown }
> This is a block quote.
> Block quote continued.
```

It renders to:
> This is a block qoute
> Block qoute continued

### Block quotes and paragraphs

To create a block qoute spanning over multiple paragraphs. Start empty lines 
with a ```>```.

``` { .markdown }
> This is the first paragraph.
>
> This is the second paragraph.
```

It renders to:

> This is the first paragraph.
>
> This is the second paragraph.

### Nested block qoutes

Nested block qoutes are created by using multiple *>*.

``` { .markdown }
> This is the first quote.
>
>> This is the nested quote.
```

It renders to:

> This is the first quote.
>
>> This is the nested quote.

## Lists

To create a unordered list start the line with a ```+```, a ```-``` or an
```*```. Each method will lead to the same result. To create a nested
list, indent the list sign with four spaces.

``` { .markdown }
* list item 1
* list item 2
* list item 3
    * list item 3.1
```

It will render to:

* list item 1
* list item 2
* list item 3
    * list item 3.1

An ordered list is created by using a number followed by a dot. Nested lists
are created by indenting the item with four spaces and the number followed by
a dot.

``` { .markdown }
1. list item 1
2. list item 2
3. list item 3
    1. list item 3.1
```

It renders to:

1. list item 1
2. list item 2
3. list item 3
    1. list item 3.1

## Tables

With pipes ```|``` markdown tables are created. Every column is sepearated 
by a pipe. To create header rows, underline them with a dash ```-```.

Here an example:
``` { .markdown }
Column 1 | Column 2 | Column 3
-------- | -------- | --------
    A1   |    B1    |    C1    
    A2   |    B2    |    C2    
    A3   |    B3    |    C3    
```

This renders to:

Column 1 | Column 2 | Column 3
-------- | -------- | --------
    A1   |    B1    |    C1    
    A2   |    B2    |    C2    
    A3   |    B3    |    C3    


## Code Blocks

You can create code blocks by enclosing the code to display between three
backticks *`*. You can start a otherwise empty line with three backticks 
to start a mulitline code block. To end the code block place three backticks
at the start of an otherwise empty line.

```` { .markdown }
 Text ```Code comes here``` text

```
Multiple 
lines
of 
code
```
````

It renders to:

Text ```Code comes here``` text

```
Multiple 
lines
of 
code
```

For a more detailed description of code blocks visit 
[the Python markdown fenced code blocks extension documentation](https://python-markdown.github.io/extensions/fenced_code_blocks/).

## Links

To add a link to your markdown document place the link title between square
braces *[]* followed by the link text in braces *()*. It has the format
```[Link text](url)```.

``` { .markdown }
[Google Search Engine](https://www.google.com)
```

This renders to:  
[Google Search Engine](https://www.google.com)

### TinyWiki Links

To provide wiki links in pages use the format ```[[slug]]```.

To create a link with an alternate link text, set the link text enclosed in
two sqaure braces followed by the slug ind round braces. It has the format 
```[[Link Text]](slug)```.

**_TinyWiki Links_ are a TinyWiki extension!**

``` { .markdown }
* [[en-tinywiki-index]]
* [[link-does-not-exist]]
* [[Django's TinyWiki Homepage]](en-tinywiki-index) 
* [[This page does not exist]](link-does-not-exist)
```

This is rendered as:

* [[en-tinywiki-index]]
* [[link-does-not-exist]]
* [[Django's TinyWiki Homepage]](en-tinywiki-index) 
* [[This page does not exist]](link-does-not-exist)



### Django Links

To add django-links use the ```$[text](app:name)``` notation. *app* is the
*app_name* value in the urls file, *name* is the name of the url and *text*
is the link text to be displayed to the user. The link is then generated by
using the function ```django.shortcuts.reverse()```.

If you need variables in the url use the ```$[text](app:name|variable|...)```
notation, where variables are seperated by a pipe ```|```.

**_Django Links_ are a TinyWiki extension and not part of the Django-Framework itself!**

Here is an example:

``` { .markdown }
* $[Homepage](tinywiki:index) 
* $[Homepage again](tinywiki:page|en-tinywiki-index)
```

* $[Homepage](tinywiki:index) 
* $[Homepage again](tinywiki:page|en-tinywiki-index)

## Images

Embedding images work by using ```![alt text](image_url)```. 

To embed wiki images use ```![[image-id]]```. 
Builtin pages can link against builtin image ids with 
```![[!builtin-image-id]]```. Negative numbers for *builtin-image-id*s are
reserved for the TinyWiki images. So use positive integers for your
*builtin-image-id*s.

**_Wiki Images_ and _Builtin Images_ are a TinyWiki extension!**


``` { .markdown }
![Picture of hemp](https://de.seedfinder.eu/pics/galerie/Serious_Seeds/AK47/17092099828694083_big.jpg)

![[---1--]]

![[!-2]]
```

![Picture of hemp](https://de.seedfinder.eu/pics/galerie/Serious_Seeds/AK47/17092099828694083_big.jpg)

![[---1--]]

![[!-2]]


To show all the linked images for a wiki page use the ```[WIKI-IMAGES]``` tag.
This tag generates a grid with the preview of your images.

Example:

``` { .markdown }
### Linked Images

[WIKI-IMAGES]
```

This renders to:

### Linked Images

[WIKI-IMAGES]

## Embedding Vidoes

``` { .markdown }
?[Django tutorial](youtube:rHux0gMZ3Eg)

?[Jellyfish]({% static 'django_tinywiki/videos/Jellyfish.mp4' %})

?[Jellyfish with width and height]({% static 'django_tinywiki/videos/Jellyfish.mp4' %}|560,315)
```

?[Django tutorial](youtube:rHux0gMZ3Eg)

?[Jellyfish]({% static 'django_tinywiki/videos/Jellyfish.mp4' %})

?[Jellyfish with width and height]({% static 'django_tinywiki/videos/Jellyfish.mp4' %}|560,315)

**Embedding Videos is a TinyWiki extension**

## Generate a *Table of Contents*

To create a dynamically created *Table of Contents* use the ```[TOC]``` tag
in a own paragraph.

**_TOC_ is a Python markdown extension!**

Example:

``` { .markdown }
...

[TOC]

...
```

It renders to  
...

[TOC]

...
