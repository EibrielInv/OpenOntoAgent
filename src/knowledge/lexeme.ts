var ds = require('datascript')

export class Lexeme {
    ontoagent:any

    constructor(ontoagent:any) {
        this.ontoagent = ontoagent
    }

    getLexemeId(lexeme_name: string) :number {
        const query = '[:find ?e :in $ ?conceptname :where [?e "lexeme" ?lexemename]]'
        const r = ds.q(query, this.ontoagent.db, lexeme_name)
        return r[0][0]
    }

    getLexemeIdOrAdd(lexeme_name: string): number {
        if (this.lexemeExists(lexeme_name)) {
            return this.getLexemeId(lexeme_name)
        } else {
            return this.addLexeme(lexeme_name)
        }
    }

    lexemeExists(lexeme_name: string) {
        const query = '[:find ?e :in $ ?lexemename :where [?e "lexeme" ?lexemename]]'
        const r = ds.q(query, this.ontoagent.db, lexeme_name)
        return r.length > 0
    }

    addLexeme(name: string) :number {
        const lexeme_id = this.ontoagent.dbAdd(null, "lexeme", name)
        return lexeme_id
    }

    addLexicalSense(lexeme_name: string, lexeme: any) :number {
        const lexeme_id = this.getLexemeIdOrAdd(lexeme_name)
        const lexicalsense_id = this.ontoagent.dbAdd(null, "sense/lexeme", lexeme_id)

        Object.keys(lexeme).forEach((k) => {
            if (k == "CAT") {
                this.ontoagent.dbAdd(lexicalsense_id, "sense/category", lexeme[k])
            } else if (k == "SYN-STRUC") {
                // Is a syntactic structure
                this.ontoagent.syntacticStructure.addSynStruc(lexeme[k], lexicalsense_id)
            } else if (k == "SEM-STRUC" && lexeme[k]!="") {
                // Is a semantic structure
                this.ontoagent.semanticStructure.addSemStruc(lexeme[k], lexicalsense_id)
            }
        })

        return lexicalsense_id
    }

    linkLexeme(property_id: number, property_name: string, lexeme:string|Array<string>) {
        if (typeof lexeme === 'string') {
            const sem_concept = this.getLexemeIdOrAdd(lexeme)
            this.ontoagent.dbAdd(property_id, property_name, sem_concept)
        } else {
            lexeme.forEach((e)=>{
                const sem_concept = this.getLexemeIdOrAdd(e)
                this.ontoagent.dbAdd(property_id, property_name, sem_concept)
            })
        }
    }
}
