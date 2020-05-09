# Table of Contents
1. [Repo Description](#Description)
2. [Markdown](#Markdown)
3. [Regular Expressions](#RegEx)

---
# Description

This repository has been my workspace for learning how to use the NLTK python libraries, regular expressions, as well as some Markdown essentials (noted in this README)

* NLTK: `nltkbasics.py`
* RegEx: `regular_expressions.py`
* Markdown: `README.md`

---
# Markdown
**Tutorial: <https://commonmark.org/help/tutorial/>**

*This is my first time creating a markdown document from scratch! To see a preview of the MD document, in VSCode command+shit+v shows a preview. Here are some more notes:*


## Emphasis

Italics: wrap text in single asterisks (*) or single underscores (_) 

Bold: wrap text in double asterisks (**) or double underscores (__)

Underline: wrap text in these tags `<ins>` and `</ins>`

## Headings

Headings are characterized by the hashtag symbol (#) and are activated
when there is a space between the hashtag(s) and the text it is meant to
create a heading out of

The more '#' the smaller the header


## Paragraphs

Can either dictate a paragraph with a \ at the end of a line (to force a newline)
or with an empty line break which is characterized by a line
that is made up of spaces, tab characters, or a new line character (enter)


## Block Quote

Start a block quote with '<'


## Lists
Use any of *, + or - to make a list. Each list must consistently use the same character. The list character requires a space after it

Ordered lists start with a number followed by a . or ) and a space. The numbers can start wherever, not necessarily at the number 1, but will start at the first number in the list specified

To nest one list within another, indent each item in the sublist by four spaces. You can also nest other elements like paragraphs, blockquotes or code blocks.

## Links

URLs may not become links in Markdown until enclosed in < and >. Turn this URL into a link:


Link text is enclosed by square brackets [], and for inline links, the link URL is enclosed by parens () directly after the [link text].

## Images

Images are almost identical to links, but an image starts with an exclamation point !.

`![](url goes here)~`

## Inline Code

Wrap inline code with backticks ` and code chunks with three ```

---

# RegEx

## Basic Notes

It's important to use a 'raw string' specification when working with regular expressions, because otherwise the use of backslashes may get mixed up in the compiler with escape characters

``` raw_string = r"Hello" ```

## Importing Regular Expressions

``` import re ```

## String searching

``` re.search(__1__,__2__) ```
1. The substring you're searching for
2. The larger string you're searching in

## Character classes

These are indicated by a square brackets inside a string `r'[]'`

``` re.search(r'[aeiou]',__2__) ```

## Match object

Match objects always have a boolean value of True.

* .string
    * The string passed to match() or search()
* .re
    * Original substring searched for
* .pos
    * Index at which RE engine began looking for a match (start index)
* .endpos
    * Index at which RE engine stopped looking for a match (end index/of string)
* .span()
    * For match object, return the 2-tuple (m.start(group), m.end(group))
* .start()
    * Index of the start of the substring matched by group
* .end()
    * Index of the end of the substring matched by group

## Inversion

The inversion concept is such that the regex search/match looks for
'anything but' what was specified. The operator `^` is used at the beginning of a bracket set to signify inversion, coupled with the bracket `[]` notation, which means that it is looking for <ins>anything except</ins> what was specified in the characters within the bracket (character class)

ie. `re.search(r'[^0-9]',"Hello")`

## Anchors

Anchors do not relate to character classes (`[]`) and rather have to do with regular string searching of a particular substring within another string.

<ins>Start of String Matching</ins>\
One notation of an anchor is the `^`, but it is used without bracket notation and at the beginning of the substring, to indicate that you are looking for a match that is a particular set of characters, such that the match has to be at the beginning of the string being searched
The anchor `^` represents the concept "the start of the string"

<ins>End of String Matching</ins>\
Another anchor notation is the `$` that is placed at the end of the substring, to confirm whether or not this substring is at the end of the string passed in.

ie. `re.search(r'ya$',"hiya")`

## Metacharacters

Special characters in strings (ie. `^`, `$`, `[]` (a character class), `-` (a range inside character class))

If you wanted to use those actual characters inside of a string, within a matching clause (ie. match the substring `[hello]`) then you would need to use escape characters to escape those special metacharacters, and "deactivate" their special meanings'

ie. `re.search(r'\[hello\]', "[hello]")` 

<ins>Other Metacharacters</ins>
* The period [`.`]
    * Means "any nonempty string"
    * If used in combination with a search, will always return a match object, if the string is not empty, or not solely a newline character
    * Can be used to indicate searching for a particular string of characters with something before, or something after (but that something doesn't matter)
    * ie. `re.search(r'a..',"adf")`
* The asterisk [`*`]
    * Means "repitition" and is a quantifier
    * When the asterisk is used, it means that the character(s) upon which the asterisk is applied (the item preceeding the `*`) can be repeated 0 or more times in the string, for a match to be found
