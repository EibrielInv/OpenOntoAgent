import {schema} from "./schema"

var ds = require('datascript')

export class Ontoagent {
    db: any
    current_id: number

    constructor() {
        this.db = ds.empty_db(schema)
        this.current_id = 1
    }

    query() {
        const query = '[:find ?e ?p ?v :where [?e ?p ?v]]'
        return ds.q(query, this.db)
    }

    addConcept(name: string, concept: any) :number {
        const concept_id = this.dbAdd(null, "concept/name", name)
        Object.keys(concept).forEach((k) => {
            if (k == "IS-A") {
                const is_a_id = this.getConceptIdOrAdd(concept[k])
                this.dbAdd(concept_id, "concept/is-a", is_a_id)
            } else {
                // Is a property
                this.addConceptProperty(k, concept[k])
            }
        })

        return concept_id
    }

    dbAdd(id:null|number, link:string|number, value:string|number|Array<string|number>) :number {
        var id_to_use: number
        if (id === null) {
            id_to_use = this.current_id
            this.current_id++
        } else {
            id_to_use = id
        }
        if (typeof value === 'string' || typeof value === 'number') {
            this.db = ds.db_with(this.db, [[":db/add", id_to_use, link, value]])
        } else if (typeof value === 'object'){
            value.forEach((e) => {
                this.db = ds.db_with(this.db, [[":db/add", id_to_use, link, e]])
            })
        } else {
            throw new Error("Value must be string, number or array");
        }

        return id_to_use
    }

    conceptExists(concept_name: string) :boolean {
        const query = '[:find ?e :in $ ?conceptname :where [?e "concept/name" ?conceptname]]'
        const r = ds.q(query, this.db, concept_name)
        return r.length > 0
    }

    getConceptId(concept_name: string) :number {
        const query = '[:find ?e :in $ ?conceptname :where [?e "concept/name" ?conceptname]]'
        const r = ds.q(query, this.db, concept_name)
        return r[0][0]
    }

    getConceptIdOrAdd(concept_name: string): number {
        if (this.conceptExists(concept_name)) {
            return this.getConceptId(concept_name)
        } else {
            return this.addConcept(concept_name, {})
        }
    }

    addConceptProperty(property_name: string, property: any) {
        const property_id = this.dbAdd(null, "concept.property/name", property_name)
        if (property["SEM"]) {
            this.linkProperty(property_id, "concept.property/semantic", property["SEM"])
        } else if (property["RELAXABLE-TO"]) {
            this.linkProperty(property_id, "concept.property/relaxable-to", property["RELAXABLE-TO"])
        } else if (property["NOT"]) {
            this.linkProperty(property_id, "concept.property/not", property["NOT"])
        }
    }

    linkProperty(property_id: number, property_name: string, concept:string|Array<string>) {
        if (typeof concept === 'string') {
            const sem_concept = this.getConceptIdOrAdd(concept)
            this.dbAdd(property_id, property_name, sem_concept)
        } else {
            concept.forEach((e)=>{
                const sem_concept = this.getConceptIdOrAdd(e)
                this.dbAdd(property_id, property_name, sem_concept)
            })
        }
    }

    // Lexemes

    getLexemeId(lexeme_name: string) :number {
        const query = '[:find ?e :in $ ?conceptname :where [?e "lexeme" ?lexemename]]'
        const r = ds.q(query, this.db, lexeme_name)
        return r[0][0]
    }

    getLexemeIdOrAdd(lexeme_name: string): number {
        if (this.lexemeExists(lexeme_name)) {
            return this.getLexemeId(lexeme_name)
        } else {
            return this.addLexeme(lexeme_name)
        }
    }

    lexemeExists(lexeme_name: string) {
        const query = '[:find ?e :in $ ?lexemename :where [?e "lexeme" ?lexemename]]'
        const r = ds.q(query, this.db, lexeme_name)
        return r.length > 0
    }

    addLexeme(name: string) :number {
        const lexeme_id = this.dbAdd(null, "lexeme", name)
        return lexeme_id
    }

    addLexicalSense(lexeme_name: string, lexeme: any) :number {
        const lexeme_id = this.getLexemeIdOrAdd(lexeme_name)
        const lexicalsense_id = this.dbAdd(null, "sense/lexeme", lexeme_id)

        Object.keys(lexeme).forEach((k) => {
            if (k == "CAT") {
                this.dbAdd(lexicalsense_id, "sense/category", lexeme[k])
            } else if (k == "SYN-STRUC") {
                // Is a syntactic structure
                this.addSynStruc(lexicalsense_id, lexeme[k])
            }
        })

        return lexicalsense_id
    }

    linkLexeme(property_id: number, property_name: string, lexeme:string|Array<string>) {
        if (typeof lexeme === 'string') {
            const sem_concept = this.getLexemeIdOrAdd(lexeme)
            this.dbAdd(property_id, property_name, sem_concept)
        } else {
            lexeme.forEach((e)=>{
                const sem_concept = this.getLexemeIdOrAdd(e)
                this.dbAdd(property_id, property_name, sem_concept)
            })
        }
    }

    // Variables

    getVariableId(variable_name: string) :number {
        const query = '[:find ?e :in $ ?variablename :where [?e "variable" ?variablename]]'
        const r = ds.q(query, this.db, variable_name)
        return r[0][0]
    }

    addVariable(name: string) :number {
        const lexeme_id = this.dbAdd(null, "variable", name)
        return lexeme_id
    }

    variableExists(variable_name: string) {
        const query = '[:find ?e :in $ ?variablename :where [?e "variable" ?variablename]]'
        const r = ds.q(query, this.db, variable_name)
        return r.length > 0
    }

    getVariableIdOrAdd(variable_name: string): number {
        if (this.variableExists(variable_name)) {
            return this.getVariableId(variable_name)
        } else {
            return this.addVariable(variable_name)
        }
    }

    linkVariable(property_id: number, property_name: string, variable:string) {
        const sem_concept = this.getVariableIdOrAdd(variable)
        this.dbAdd(property_id, property_name, sem_concept)
    }

    // Syntactic structure

    addSynStruc(lexicalsense_id: number, synstruc: any) :number {
        const synstruc_id = this.dbAdd(null, "syntactic-structure/id", lexicalsense_id)

        for (let n=0; n<synstruc.length; n++) {
            const element = synstruc[n]
            if (element["NAME"] == "CAT") {
                this.dbAdd(synstruc_id, "syntactic-structure/category", element["VALUE"])
            } else if (element["NAME"] == "TYPE") {
                this.dbAdd(synstruc_id, "syntactic-structure/type", element["VALUE"])
            } else if (element["NAME"] == "TENSE") {
                this.dbAdd(synstruc_id, "syntactic-structure/tense", element["VALUE"])
            } else if (element["NAME"] == "NUMBER") {
                this.dbAdd(synstruc_id, "syntactic-structure/number", element["VALUE"])
            } else if (element["NAME"] == "OPT") {
                if (element["VALUE"] == "+") {
                    this.dbAdd(synstruc_id, "syntactic-structure/optional", 1)
                }
            } else if (element["NAME"] == "ROOT-WORD") {
                this.linkLexeme(synstruc_id, "syntactic-structure/root-word", element["VALUE"])
            } else if (element["NAME"] == "ROOT") {
                this.linkVariable(synstruc_id, "syntactic-structure/root", element["VALUE"])
            }
        }

        return synstruc_id
    }
}
