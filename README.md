# OpenOntoAgent
Experimental and simplified OntoAgent architecture. Released as Open Source code.
0
Inspired by the book [Linguistics for the Age of AI](https://mitpress.mit.edu/books/linguistics-age-ai) by Marjorie McShane and Sergei Nirenburg, and aditional literature.

## OntoAgent inversed
The main goal for this project is not Natural Language Processing, but Natural Language Generation.


OpenOntoAgent should drive a [TokenMenu](https://medium.com/eibriel/a-new-conversational-ui-32c3c085b64c) interface, allowing human machine interaction. The software generates candidate inputs, and the user selects the desired one.

This project will still use TMR, and a knowledge graph, but not a Lexicon (no syntactic structures). Instead the TMRs will feed directly a realization engine that will turn them into natural language.

The work of the Lexicon will be offloaded to the Knowledge base (semantic structure) and the realization engine (syntactic structure).

To emphatize the importance of the TokenMenu all the information will be feed into the system as TMRs.

[Datascript](https://github.com/tonsky/datascript/) will be used to store and manipulate the data.


## Dogfooding
The first application for this library should be allowing the use of the TokenMenu to add Concepts and rules for the realization engine.
