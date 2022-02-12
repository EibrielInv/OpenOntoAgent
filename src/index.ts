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
                let is_a_id: number
                if (!this.conceptExists(concept[k])) {
                    is_a_id = this.addConcept(concept[k], {})
                } else {
                    is_a_id = this.getConceptId(concept[k])
                }
                this.dbAdd(concept_id, "concept/is-a", is_a_id)
            } else {
                // Is a property

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
        return r[0]
    }

    addConceptProperty() {
        
    }
}
