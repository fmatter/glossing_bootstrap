# Bootstrapping morphological glossing for underresourced languages
 A challenge for the DH@unibe NLP-Hackathon 2021 
## Introduction
There are around 6000-7000 human languages in the world, but NLP tools have only been developed for a fraction of them.
While language-independent tools exist, they are often not interested in the same kinds of problems as traditional linguistics, which among other things investigates linguistic diversity.
A central part of structural linguistics is grammatical or morphological analysis, a process which can be applied to any spoken human language.
Morphological analysis establishes the smallest meaning-carrying unit in a language, called [morphemes](https://en.wikipedia.org/wiki/Morpheme).
Word forms are conceptualized as being composed of morphemes, so e.g. the English word form *conceptualized* consists of:
1. the root *concept*
1. the adjectivizer *-ual*
1. the verbalizer *-ize*
1. the past marker *-d*

For large languages, there are either models trained on large corpora or explicitly modelled implementations of the morphological structure of a language.
For small languages (which are usually at least as interesting as the large ones), no such tools exist, due to the lack of available large corpora and the cost of creating detailed language-specific models.

## Interlinear text
A common way of representing morphological structure in linguistics is interlinearized glossed text (IGT).
It minimally consists of a object language line, a morpheme-by-morpheme glossing, and a free translation.
Here is an example from the Oceanic language [Unua](https://glottolog.org/resource/languoid/id/unua1237) (from [Pierce 2015](https://doi.org/10.1515/9781614516590): 249):

<!-- Vin nge iravi dabangon ngo imrebe? -->

```
(1) βin   ŋe   i-ɾav-i     dabaŋo-n  ŋo  i-mɾebe 
    woman PROX 3SG-take-TR belly-3SG DEM 3SG-how 
    'How did this woman get that belly?'
```
In the (minimalistic) approach to morphological structure used here, there are three kinds of morphemes:

1. **roots** usually carry lexical meaning and form the core of word forms
2. **prefixes** are smaller, bound morphemes which occur before a stem
3. **suffixes** are smaller bound morphemes which occur after a stem

(A stem is a combination of morphemes; it can consist of either a bare root, or a root with prefixes and/or suffixes.)
So in the Unua example above, the following morphemes can be identified:

|Form|Gloss|
|:-|:-|
|βin|woman|
|dabaŋo|belly|
|ɾav|take|
|mɾebe|how|
|ŋe|PROX|
|ŋo|DEM|
|i-|3SG|
|-i|TR|
|-n|3SG|

Roots, pre- and suffixes are combined to grammatical words, or g-words.
What is delimited by spaces in a sentence -- intuitively a 'word' to most people -- is strictly speaking a phonological word (p-word).
Multiple g-words can be combined into a single p-word, think for example of the English (p-)words *mustn't* or *I've*, which contain the g-words *must* and *not* and *I* and *have*, respectively.
Sometimes, these g-words in turn contain multiple morphemes, as in the following example from the Pama-Nyungan language [Ngiyambaa](https://glottolog.org/resource/languoid/id/wang1291) ([Donaldson 1980](http://hdl.handle.net/11858/00-001M-0000-0012-9923-3): 131):

<!-- ŋayagadhi:ndugal -->

```
(2) ŋa-j-aka=t̪iː=ntu-kal     
    see-CONJ-IRR=1OBL=2NOM-PL 
    You all will see me.'
```


Here, there are three distinct word forms: *ŋajaka*, *t̪iː*, and *ntukal*, which can be further segmented as *ŋa-j-aka*, *t̪iː*, and *ntu-kal*, respectively.
As you can see in (2), g-words within a larger p-word are delimited with `=`, just like morphemes inside a g-word are delimited with `-`.

<!-- manhaŋ-gu=naŋ-gal ŋima-nhi
white.paint-INS=3ABS-PL paint-INTR.PST
'They were painted with white paint.'
311

jawaã-t͡ʃau=ita-ha-i
dog-NEG.REL=be-1SG-DECL
'I am not a dog.'
68

W-ari-bat̻bit̻-pe=w-iri
3PL.S-poke.IRR-sew-FUT=3PL.S-sit.IRR
'They will be sewing.'
reid 256 -->

## The task
You are given a list of morphemes from an underresourced language, as well as a list of sentences (or single words).
Your task is to divide the provided word forms into the known morphemes.
The morphemes are provided as a list of form-meaning pairs, as in the table above.
That is, prefixes and suffixes are identified by preceding and following hyphens, and roots do not have hyphens.
The sentences are provided as space-delimited word forms, but boundaries between g-words of the same p-word are not indicated by `=`.

Your solution should be able to deal with morpheme lists and word forms from any language, so no language-specific morphemes or combinations thereof should be encoded.

TODO: datasets