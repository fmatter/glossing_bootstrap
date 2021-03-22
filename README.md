# Bootstrapping morphological glossing for underresourced languages
 A challenge for the DH@unibe NLP-Hackathon 2021 
# Introduction
There are around 6000-7000 human languages in the world, but NLP tools have only been developed for a fraction of them.
While language-independent tools exist, they are often not interested in the same kinds of problems as traditional linguistics, which among other things investigates linguistic diversity.
A central part of structural linguistics is grammatical or morphological analysis, a process which can be applied to any spoken human language.
Morphological analysis establishes the smallest meaning-carrying unit in a language, called [morphemes](https://en.wikipedia.org/wiki/Morpheme).
Word forms are conceptualized as being composed of morphemes, so e.g. the form *conceptualized* consists of:
* the root *concept*
* the adjectivizer *-ual*
* the verbalizer *-ize*
* the past marker *-ed*

For large languages, there are either models trained on large corpora or specific descriptions of the morphological structure of a language.
For small languages (which are usually at least as interesting as the large ones), no such tools exist, due to the lack of available large corpora and the cost of creating detailed language-specific models.
A common way of representing morphological structure in linguistics is interlinearized glossed text (IGT).
It minimally consists of a object language line, a morpheme-by-morpheme glossing, and a free translation.
Here is an example from the Oceanic language [Unua](https://glottolog.org/resource/languoid/id/unua1237) (from [Pierce 2015](https://doi.org/10.1515/9781614516590): 249):

Vin nge iravi dabangon ngo imrebe?
|***βin***|***ŋe***|***i-ɾav-i***|***dabaŋo-n***|***ŋo***|***i-mɾebe***|
|:-|:-|:-|:-|:-|:-|
|woman|PROX|3SG-take-TR|belly-3SG|DEM|3SG-how|

'How did this woman get that belly?'


# The task
You are given a list of morphemes from an underresourced language, and a list of words, or sentences containing multiple words.
In the (minimalistic) approach to morphological structure used here, there are three kinds of morphemes:

1. **roots** usually carry lexical meaning and form the core of word forms
2. **prefixes** are smaller, bound morphemes which occur before a stem
3. **suffixes** are smaller bound morphemes which occur after a stem

These are provided as a list of form-meaning pairs, with prefixes and suffixes being identified with preceding or following hyphens, respectively.
Here's how that would look for the Unua example above:

|Form|Gloss|
|:-|:-|
|βin|woman|
|ŋe|PROX|
|i-|3SG|
|ɾav|take|
|-i|TR|
|dabaŋo|belly|
|-n|3SG|
|ŋo|DEM|
|mɾebe|how|

Your task is to divide the provided words into the known morphemes.
A stem is a combination of morphemes; it can consist of either a bare root, or a root with prefixes and/or suffixes.