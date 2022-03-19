import {OntologyDB, LexiconDB} from "../src/types"
import {Ontoagent, Ontogen} from "../src/index"

import {ontology, lexicon, tmr} from "../src/knowledge/squirrel"

var ds = require('datascript')

test("Ontogen", () => {
    const o = new Ontoagent()

    Object.keys(ontology as OntologyDB).forEach((k:string) => {
        o.concept.addConcept(k, ontology[k])
    })

    const result = [
        ["INGESTIBLE-MEDICATION"],
        ["INGEST"],
        ["BEVERAGE"],
        ["SOLID"],
        ["FOOD"],
        ["ORGANISM"],
        ["ANIMAL"],
        ["SQUIRREL"],
        ["NUT-FOODSTUFF"],
    ]

    const query = '[:find ?name :where [_ "concept/name" ?name]]'

    expect(ds.q(query, o.db)).toBeSameDB(result)

})

test("Ontogen", () => {
    const o = new Ontoagent()

    Object.keys(ontology as OntologyDB).forEach((k:string) => {
        o.concept.addConcept(k, ontology[k])
    })

    Object.keys(lexicon as LexiconDB).forEach((k:string) => {
        o.lexeme.addLexeme(k)
        Object.keys(lexicon[k]).forEach((kk:string) => {
            o.lexeme.addLexicalSense(kk, lexicon[k][kk])
        })
    })

    o.tmr.addTmr(tmr["TMR"])

    const result = [
        ["INGEST"],
        ["SQUIRREL"],
        ["NUT-FOODSTUFF"],
    ]

    const gen = new Ontogen(o)

    expect(gen.getTMRConcepts(1)).toBeSameDB(result)

})
