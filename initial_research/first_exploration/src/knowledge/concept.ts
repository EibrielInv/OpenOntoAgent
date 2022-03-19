import {ConceptDB} from "../types"
var ds = require('datascript')

export class Concept {
    ontoagent:any

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
    }

    addConcept(name: string, concept: ConceptDB) :number {
        const concept_id = this.ontoagent.dbAdd(null, "concept/name", name)
        Object.keys(concept).forEach((k) => {
            if (k == "IS-A") {
                const is_a_id = this.getConceptIdOrAdd(concept[k] as string)
                this.ontoagent.dbAdd(concept_id, "concept/is-a", is_a_id)
            } else {
                // Is a property
                this.addConceptProperty(k, concept[k], concept_id)
            }
        })

        return concept_id
    }

    conceptExists(concept_name: string) :boolean {
        const query = '[:find ?e :in $ ?conceptname :where [?e "concept/name" ?conceptname]]'
        const r = ds.q(query, this.ontoagent.db, concept_name)
        return r.length > 0
    }

    getConceptId(concept_name: string) :number {
        const query = '[:find ?e :in $ ?conceptname :where [?e "concept/name" ?conceptname]]'
        const r = ds.q(query, this.ontoagent.db, concept_name)
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
        const property_id = this.ontoagent.dbAdd(null, "concept.property/name", property_name)
        this.ontoagent.dbAdd(concept_id, "concept/property", property_id)
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
            this.ontoagent.dbAdd(property_id, property_name, sem_concept)
        } else {
            concept.forEach((e)=>{
                const sem_concept = this.getConceptIdOrAdd(e)
                this.ontoagent.dbAdd(property_id, property_name, sem_concept)
            })
        }
    }
}
