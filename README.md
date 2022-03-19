# OpenOntoAgent
Experimental and incomplete OntoAgent architecture. Released as Open Source code.


Inspired by the book [Linguistics for the Age of AI](https://mitpress.mit.edu/books/linguistics-age-ai) by Marjorie McShane and Sergei Nirenburg, and aditional literature.


Using OWL was promising, but looks like each Lexical Sense should be a OWL Class, that don't seems entirely right.

Lexical Senses imposes constraints (syntactic structure), and modify the values of other elements (semantic structure, meaning procedures).

- The program should always terminate?
- Decidability?


> A critical element addressed in the implementation of OntoGraph was usability. In contrast to
other knowledge bases – for example, SCONE, which is written in LISP, or OWL
(https://www.w3.org/2001/sw/wiki/OWL), a semantic web language – the OntoGraph API is writ-
ten in Python in such a way that using it would feel like using common Python builtins. For exam-
ple, the OntoGraph Frame object has near-identical behavior to Python's default dict object, though
it adds automatic inheritance, relation crawling, and data persistence, among other operations. This
emphasis on usability promises faster ramp-up times for both developers and knowledge acquirers.
Implementation in Python also allowed for a variety of other benefits: property values (frame slot
fillers) can be nearly any data type handled by any modern programming language, and they can,
importantly, include executable code as well. With its object-oriented approach, OntoGraph allows
for individual frames to extend the Frame class, thus giving knowledge elements custom program-
matic capabilities.

## Datalog

- E P V
- Pull API (EQL - Phantom)
- Datascript
- Datomic
- https://bit.ly/datalog-gist


Factual Vs. Structural definitions

Looks like Datascript is the way to go!


## Semantic structure (and patterns)

The issue with this is that is not typed
- Is OBSEQUIOUS a concept?
- Does THEME expect a concept or value?

Also semantic structure is more code than data

```
"REQUEST-ACTION": {
    "FORMALITY": "OBSEQUIOUS",
    "AGENT": {"VALUE": "^$VAR1"},
    "THEME": {"VALUE": "^$VAR7", "BENEFICIARY": {"VALUE": "^$VAR8"}},
}
```

Solution: using expression evaluation: https://ericsmekens.github.io/jsep/

```
ra = new Concept("REQUEST-ACTION")
ra.formality.set("OBSEQUIOUS")
ra.property("AGENT").set(lexeme("VAR1").concept)
ra.property("THEME").set(lexeme("VAR7").concept)
ra.property("THEME").property("BENEFICIARY").set(lexeme("VAR8").concept)
```

Should concept properties be predefined (part of the scheme)? - Most probably not

### Patters

**Something ingesting something**
```
ingest = new Instance("INGEST")
ingest.property("AGENT").set("*")
ingest.property("THEME").set("*")
```

**Something brown ingesting something**
```
ingest = new Instance("INGEST")
ingest.property("AGENT").set("*")
ingest.property("AGENT").property("COLOR").set("BROWN")
ingest.property("THEME").set("*")
```

**Something ingesting a nut**
```
ingest = new Instance("INGEST")
ingest.property("AGENT").set("*")
nut = new Instance("NUT-FOODSTUFF")
ingest.property("THEME").set(nut)
```

**Event where a squirrel is the agent**
```
event = new Instance("EVENT", true) // EVENT or child
squirrel = new Instance("SQUIRREL")
event.property("AGENT").set(squirrel)
event.property("THEME").set("*")
```

## Dogfooding

Use OpenOntoAgent to parse partially anotated natural language sentence into TMRs, knowledge and rules

## Lexicon

Remove lexicon, in favor of rules to directly generate text from TMR
