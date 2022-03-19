
export class Tmr {
    ontoagent:any
    current_tmr_id: number

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
        this.current_tmr_id = 1
    }

    addTmr(tmr:any) {
        const tmr_id = this.ontoagent.dbAdd(null, "tmr/id", this.current_tmr_id)
        this.current_tmr_id++
        Object.keys(tmr).forEach((k)=>{
            const instance_id = this.addTmrInstance(k, tmr[k], tmr_id)
        })
    }

    // TODO: Some elements should be ordered
    addTmrInstance(instance_name:string, instance:any, tmr_id:number) {
        const instance_id = this.ontoagent.dbAdd(null, "tmr.instance/id", instance_name)
        this.ontoagent.dbAdd(tmr_id, "tmr/instance", instance_id)
        Object.keys(instance).forEach((k)=>{
            this.ontoagent.semanticStructure.addSemStrucConceptProperty(k, instance[k], instance_id)
        })
        return instance_id
    }
}
