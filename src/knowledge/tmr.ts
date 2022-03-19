
export class Tmr {
    ontoagent:any
    current_tmr_id: number

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
        this.current_tmr_id = 1
    }

    addTmr(tmr:any) {
        const tmr_id = this.ontoagent.datascript.dbAdd(null, "tmr/id", this.current_tmr_id)
        this.current_tmr_id++
        Object.keys(tmr).forEach((k)=>{
            const instance_id = this.addTmrInstance(k, tmr[k], tmr_id)
        })
    }

    // TODO: Some elements should be ordered
    addTmrInstance(instance_name:string, instance:any, tmr_id:number) {
        const instance_id = this.ontoagent.datascript.dbAdd(null, "tmr.instance/id", instance_name)
        this.ontoagent.datascript.dbAdd(tmr_id, "tmr/instance", instance_id)
        Object.keys(instance).forEach((k)=>{
            this.addTmrInstanceProperty(k, instance[k], instance_id)
        })
        return instance_id
    }

    addTmrInstanceProperty(concept_name: string, properties: any, lexicalsense_id: number) {
        const ssproperty_id = this.ontoagent.datascript.dbAdd(null, "tmr.instance.property/name", concept_name)
        this.ontoagent.datascript.dbAdd(lexicalsense_id, "tmr.instance.property/property", ssproperty_id)
        if (typeof properties === 'string') {
            this.ontoagent.datascript.dbAdd(ssproperty_id, "tmr.instance.property/value", properties)
            return ssproperty_id
        }

        if (properties === null) {
            return ssproperty_id
        }

        Object.keys(properties).forEach((k)=>{
            this.addTmrInstanceProperty(k, properties[k], ssproperty_id)
        })

        return ssproperty_id
    }
}
