# TinyWiki Markdown Syntax

## Table of contents

[TOC]

## Introduction

*Markdown* is a simple markup language that allows to render it content in
*HTML*. *TinyWiki* uses *Markdown* for its Wiki-pages. *Github* for example
uses *Markdown* too for its README-files.

This short guide gives you an overview of the *Markdown*-syntax.

## Headings

To create a headings in *Markdown*, start the line with atleast one hash sign
(*#*) followed by a space. The number of hash signs define the level of the
heading.

```
# Heading Level 1

## Heading Level 2

### Heading Level 3

#### Heading Level 4

##### Heading Level 5

###### Heading Level 6
```

### Alternate syntax

To create a level 1 heading you can underline the heading text with any number
of equal signs (*=*). For level 2 can be created by underlining the text with
any number dashes (*-*).

```
Heading Level 1
===============

Heading Level 2
---------------
```

## Paragraphs and Line breaks

To create a paragraph use atleast one empty line between one or more lines of 
text. To create a line break end the line with two or more spaces.

### Expamle
```
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
```
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

## Blockquotes

To add a blockquote, place a *>* in front of a paragraph.

```
> This is a block quote.
> Block quote continued.
```

It renders to:
> This is a block qoute
> Block qoute continued

### Block quotes and paragraphs

To create a block qoute spanning over multiple paragraphs. Start empty lines 
with a *>*.

```
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

```
> This is the first quote.
>
>> This is the nested quote.
```

It renders to:
> This is the first quote.
>
>> This is the nested quote.

## Lists

To create a unordered list start the line with a *plus*, a *dash* or an
*asterisk*. Each method will lead to the same result. To create a nested
list, indent the list sign with four spaces.

```markdown
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

```markdown
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

With pipes (```|```) markdown tables are created. Every column is sepearated 
by a pyipe. To create header rows, underline them with a dash ```-```.

Here an example:
```
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

```
 ``` Code comes here ```

 ``` { .markdown }

 Multiple 
 lines
 of 
 code
 ```
```

It redners to:  
``` Code comes here ```

``` { .markdown }
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

```
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

Here is an example:

```
* $[Homepage](tinywiki:index) 
* $[Homepage again](tinywiki:page|en-tinywiki-index)
```

* $[Homepage](tinywiki:index) 
* $[Homepage again](tinywiki:page|en-tinywiki-index)

## Images

Embedding images work by using ```![alt text](image_url)```. To embed wiki images
use ```![[image-id]]```.

```
![Picture of hemp](https://de.seedfinder.eu/pics/galerie/Serious_Seeds/AK47/17092099828694083_big.jpg)

![[--1--]]
```

![Picture of hemp](https://de.seedfinder.eu/pics/galerie/Serious_Seeds/AK47/17092099828694083_big.jpg)

![[--1--]]


**TODO**
