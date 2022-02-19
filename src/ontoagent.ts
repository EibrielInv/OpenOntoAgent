import {schema} from "./schema"
import {Concept} from "./concept"
import {Lexeme} from "./lexeme"
import {SemanticStructure} from "./semantic-structure"
import {SyntacticStructure} from "./syntactic-structure"
import {Tmr} from "./tmr"

var ds = require('datascript')

export class Ontoagent {
    db:any
    concept:Concept
    lexeme:Lexeme
    semanticStructure:SemanticStructure
    syntacticStructure:SyntacticStructure
    tmr:Tmr

    current_id:number

    constructor() {
        this.db = ds.empty_db(schema)
        this.current_id = 1

        this.concept = new Concept(this)
        this.lexeme = new Lexeme(this)
        this.semanticStructure = new SemanticStructure(this)
        this.syntacticStructure = new SyntacticStructure(this)
        this.tmr = new Tmr(this)
    }

    query() {
        const query = '[:find ?e ?p ?v :where [?e ?p ?v]]'
        return ds.q(query, this.db)
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

}
