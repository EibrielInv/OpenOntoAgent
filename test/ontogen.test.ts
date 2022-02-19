import {OntologyDB, LexiconDB} from "../src/types"
import {Ontoagent} from "../src/index"

import {ontology, lexicon} from "../src/squirrel"

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

    const result = [["EAT-V1"]]

    const query = '[ \
        :find ?lexemename \
        :in $ ?conceptname \
        :where \
        [?l, "lexeme", ?lexemename] \
        [?s, "sense/lexeme", ?l]\
        [?s, "sense/semantic-structure", ?ss] \
        [?ss "semantic-structure.concept.property/property" ?p] \
        [?p "semantic-structure.concept.property/name" ?conceptname]\
    ]'

    expect(ds.q(query, o.db, "INGEST")).toBeSameDB(result)

})
