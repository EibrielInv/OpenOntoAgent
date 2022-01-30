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
