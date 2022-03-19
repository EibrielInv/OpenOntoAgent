import {Datascript} from "../datascript"
import {Concept} from "./concept"
import {SemanticStructure} from "./semantic-structure"
import {Tmr} from "./tmr"

export class Ontoagent {
    datascript:Datascript

    concept:Concept
    semanticStructure:SemanticStructure
    tmr:Tmr

    constructor() {
        this.datascript = new Datascript()

        this.concept = new Concept(this)
        this.semanticStructure = new SemanticStructure(this)
        this.tmr = new Tmr(this)
    }

}
