var ds = require('datascript')

export class Ontogen {
    ontoagent:any

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
    }

    getTMRConcepts(tmrId:number) {
        const query = '[ \
            :find ?n \
            :in $ ?tmrid \
            :where \
            [?ti "tmr/id" ?tmrid] \
            [?ti "tmr/instance" ?sp], \
            [?sp "semantic-structure.concept.property/property" ?t] \
            [?t "semantic-structure.concept.property/name" "CONCEPT"] \
            [?t "semantic-structure.concept.property/value" ?n] \
        ]'

        return ds.q(query, this.ontoagent.db, tmrId)
    }

}
