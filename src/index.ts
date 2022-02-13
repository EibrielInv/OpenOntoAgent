import {schema} from "./schema"

var ds = require('datascript')

export class Ontoagent {
    db: any
    current_id: number
    current_synstruc_id: number
    current_semstruc_id: number

    constructor() {
        this.db = ds.empty_db(schema)
        this.current_id = 1
        this.current_synstruc_id = 1
        this.current_semstruc_id = 1
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
                this.addConceptProperty(k, concept[k], concept_id)
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

    addConceptProperty(property_name: string, property: any, concept_id: number) {
        const property_id = this.dbAdd(null, "concept.property/name", property_name)
        this.dbAdd(concept_id, "concept/property", property_id)
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
                this.addSynStruc(lexeme[k], lexicalsense_id)
            } else if (k == "SEM-STRUC" && lexeme[k]!="") {
                // Is a semantic structure
                this.addSemStruc(lexeme[k], lexicalsense_id)
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

    getVariableId(variable_name: string, lexicalsense_id: number) :number {
        const query = '[:find ?e :in $ ?variablename ?senseid :where [?e "variable/name" ?variablename] [?e "variable/sense.ref" ?senseid]]'
        const r = ds.q(query, this.db, variable_name, lexicalsense_id)
        return r[0][0]
    }

    addVariable(name: string, lexicalsense_id: number) :number {
        const variable_id = this.dbAdd(null, "variable/name", name)
        this.dbAdd(variable_id, "variable/sense.ref", lexicalsense_id)
        return variable_id
    }

    variableExists(variable_name: string, lexicalsense_id: number) {
        const query = '[:find ?e :in $ ?variablename ?senseid :where [?e "variable/name" ?variablename] [?e "variable/sense.ref" ?senseid]]'
        const r = ds.q(query, this.db, variable_name, lexicalsense_id)
        return r.length > 0
    }

    getVariableIdOrAdd(variable_name: string, lexicalsense_id: number): number {
        if (this.variableExists(variable_name, lexicalsense_id)) {
            return this.getVariableId(variable_name, lexicalsense_id)
        } else {
            return this.addVariable(variable_name, lexicalsense_id)
        }
    }

    linkVariable(property_id: number, property_name: string, variable: string, lexicalsense_id: number) {
        const sem_concept = this.getVariableIdOrAdd(variable, lexicalsense_id)
        this.dbAdd(property_id, property_name, sem_concept)
    }

    // Syntactic structure

    addSynStruc(synstruc: any, lexicalsense_id: number) :number {
        const synstruc_id = this.dbAdd(null, "syntactic-structure/id", this.current_synstruc_id)
        this.current_synstruc_id++
        this.dbAdd(lexicalsense_id, "sense/syntactic-structure", synstruc_id)

        for (let n=0; n<synstruc.length; n++) {
            const name = Object.keys(synstruc[n])[0]
            const value = synstruc[n][name]
            if (name == "CAT") {
                this.dbAdd(synstruc_id, "syntactic-structure/category", value)
            } else if (name == "TYPE") {
                this.dbAdd(synstruc_id, "syntactic-structure/type", value)
            } else if (name == "TENSE") {
                this.dbAdd(synstruc_id, "syntactic-structure/tense", value)
            } else if (name == "NUMBER") {
                this.dbAdd(synstruc_id, "syntactic-structure/number", value)
            } else if (name == "OPT") {
                if (value == "+") {
                    this.dbAdd(synstruc_id, "syntactic-structure/optional", 1)
                }
            } else if (name == "ROOT-WORD") {
                this.linkLexeme(synstruc_id, "syntactic-structure/root-word", value)
            } else if (name == "ROOT") {
                this.linkVariable(synstruc_id, "syntactic-structure/root", value, lexicalsense_id)
            } else {
                if (typeof value === 'string') {
                    this.dbAdd(synstruc_id, "syntactic-structure/value", value)
                } else {
                    // Is an object
                    const synstruc2_id = this.addSynStruc(value, lexicalsense_id)
                    this.dbAdd(synstruc_id, "syntactic-structure/object", synstruc2_id)
                }
            }
        }

        return synstruc_id
    }


    // Semantic structure

    addSemStruc(semstruc: any, lexicalsense_id: number) :number {
        const semstruc_id = this.dbAdd(null, "semantic-structure/id", this.current_semstruc_id)
        this.current_semstruc_id++
        this.dbAdd(lexicalsense_id, "sense/semantic-structure", semstruc_id)

        if (typeof semstruc === 'string') {
            this.addSemStrucConceptProperty(semstruc, null, semstruc_id)
        } else {
            Object.keys(semstruc).forEach((k)=>{
                this.addSemStrucConceptProperty(k, semstruc[k], semstruc_id)
            })
        }

        return semstruc_id
    }

    addSemStrucConceptProperty(concept_name: string, properties: any, lexicalsense_id: number) {
        const ssproperty_id = this.dbAdd(null, "semantic-structure.concept.property/name", concept_name)
        this.dbAdd(lexicalsense_id, "semantic-structure.concept.property/property", ssproperty_id)
        if (typeof properties === 'string') {
            this.dbAdd(ssproperty_id, "semantic-structure.concept.property/value", properties)
            return ssproperty_id
        }

        if (properties === null) {
            return ssproperty_id
        }

        Object.keys(properties).forEach((k)=>{
            this.addSemStrucConceptProperty(k, properties[k], ssproperty_id)
        })

        return ssproperty_id
    }
}
