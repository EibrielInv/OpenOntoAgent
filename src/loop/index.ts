import {schema} from "./schema"

var ds = require('datascript')

export class Loop {
    db:any
    pattern_graph:any
    current_id:number

    constructor() {
        this.db = ds.empty_db(schema)
        this.current_id = 1
        this.pattern_graph =
        {
            "INGEST-1":
                {"AGENT:*-1":
                    {"THEME:*-1":
                        "TIME:FIND-ANCHOR-TIME"
                }
            }
        }

        const pattern = ""
        /*
        Something ingesting something
        Something brown ingesting something
        Something ingesting a nut
        Event where a squirrel is the agent

        A pattern is a graph

        The TMR is turned into a query to find matches
        */

        // Pattern
        // Something ingesting something
        const id = this.dbAdd(null, "pattern", 1)
        this.dbAdd(id, "pattern/instance", 1)
        const concept_id = this.dbAdd(null, "concept", 1)
        this.dbAdd(id, "pattern.instance/concept", concept_id)
        this.dbAdd(id, "concept/name", "INGEST")
        this.dbAdd(id, "concept/agent", "*")
    }

    // BOILERPLATED
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

    match(input_tmr: any, start:Array<string>=[]) {

    }
}
