var ds = require('datascript')

export class Variable {
    ontoagent:any

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
    }

    getVariableId(variable_name: string, lexicalsense_id: number) :number {
        const query = '[:find ?e :in $ ?variablename ?senseid :where [?e "variable/name" ?variablename] [?e "variable/sense.ref" ?senseid]]'
        const r = ds.q(query, this.ontoagent.db, variable_name, lexicalsense_id)
        return r[0][0]
    }

    addVariable(name: string, lexicalsense_id: number) :number {
        const variable_id = this.ontoagent.dbAdd(null, "variable/name", name)
        this.ontoagent.dbAdd(variable_id, "variable/sense.ref", lexicalsense_id)
        return variable_id
    }

    variableExists(variable_name: string, lexicalsense_id: number) {
        const query = '[:find ?e :in $ ?variablename ?senseid :where [?e "variable/name" ?variablename] [?e "variable/sense.ref" ?senseid]]'
        const r = ds.q(query, this.ontoagent.db, variable_name, lexicalsense_id)
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
        this.ontoagent.dbAdd(property_id, property_name, sem_concept)
    }
}
