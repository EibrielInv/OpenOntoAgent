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

    dbAdd(id:null|number, link:string|number, value:string|number) :number {
        var id_to_use: number
        if (id === null) {
            id_to_use = this.current_id
            this.current_id++
        } else {
            id_to_use = id
        }
        this.db = ds.db_with(this.db, [[":db/add", id_to_use, link, value]])

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
}
