export class SemanticStructure {
    ontoagent:any
    current_semstruc_id: number

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
        this.current_semstruc_id = 1
    }

    addSemStruc(semstruc: any, lexicalsense_id: number) :number {
        const semstruc_id = this.ontoagent.dbAdd(null, "semantic-structure/id", this.current_semstruc_id)
        this.current_semstruc_id++
        this.ontoagent.dbAdd(lexicalsense_id, "sense/semantic-structure", semstruc_id)

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
        const ssproperty_id = this.ontoagent.dbAdd(null, "semantic-structure.concept.property/name", concept_name)
        this.ontoagent.dbAdd(lexicalsense_id, "semantic-structure.concept.property/property", ssproperty_id)
        if (typeof properties === 'string') {
            this.ontoagent.dbAdd(ssproperty_id, "semantic-structure.concept.property/value", properties)
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
