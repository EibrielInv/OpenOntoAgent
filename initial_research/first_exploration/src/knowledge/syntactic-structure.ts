
import {Variable} from "./variable"

export class SyntacticStructure {
    ontoagent:any
    variable:Variable
    current_synstruc_id: number

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
        this.variable = new Variable(ontoagent)
        this.current_synstruc_id = 1
    }

    addSynStruc(synstruc: any, lexicalsense_id: number) :number {
        const synstruc_id = this.ontoagent.dbAdd(null, "syntactic-structure/id", this.current_synstruc_id)
        this.current_synstruc_id++
        this.ontoagent.dbAdd(lexicalsense_id, "sense/syntactic-structure", synstruc_id)

        for (let n=0; n<synstruc.length; n++) {
            const name = Object.keys(synstruc[n])[0]
            const value = synstruc[n][name]
            if (name == "CAT") {
                this.ontoagent.dbAdd(synstruc_id, "syntactic-structure/category", value)
            } else if (name == "TYPE") {
                this.ontoagent.dbAdd(synstruc_id, "syntactic-structure/type", value)
            } else if (name == "TENSE") {
                this.ontoagent.dbAdd(synstruc_id, "syntactic-structure/tense", value)
            } else if (name == "NUMBER") {
                this.ontoagent.dbAdd(synstruc_id, "syntactic-structure/number", value)
            } else if (name == "OPT") {
                if (value == "+") {
                    this.ontoagent.dbAdd(synstruc_id, "syntactic-structure/optional", 1)
                }
            } else if (name == "ROOT-WORD") {
                this.ontoagent.lexeme.linkLexeme(synstruc_id, "syntactic-structure/root-word", value)
            } else if (name == "ROOT") {
                this.variable.linkVariable(synstruc_id, "syntactic-structure/root", value, lexicalsense_id)
            } else {
                if (typeof value === 'string') {
                    this.ontoagent.dbAdd(synstruc_id, "syntactic-structure/value", value)
                } else {
                    // Is an object
                    const synstruc2_id = this.addSynStruc(value, lexicalsense_id)
                    this.ontoagent.dbAdd(synstruc_id, "syntactic-structure/object", synstruc2_id)
                }
            }
        }

        return synstruc_id
    }
}
