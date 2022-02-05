import {schema} from "./schema"

var ds = require('datascript');

export class Ontoagent {
    db: any
    constructor() {
        this.db = ds.empty_db(schema);
        this.db = ds.db_with(this.db, [[":db/add", 1, "concept/name", "animal"]]);
    }

    query() {
        const query = '[:find ?e ?p ?v :where [?e ?p ?v]]'
        return ds.q(query, this.db);
    }
}
