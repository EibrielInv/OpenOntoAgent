
export interface ConceptPropertiesDB {
    [key: string]: string|Array<string>
}

export interface ConceptDB {
    [key: string]: ConceptPropertiesDB | string
}

export interface OntologyDB {
    [key: string]: ConceptDB
}

//

export interface LexiconDB {
    [key: string]: {
        [key: string]: {
            "CAT"?: string,
            "DEF"?: string,
            "EX"?: string,
            "COMMENTS"?: string,
            "TMR-HEAD"?: string,
            "SYN-STRUC": {

            } | string,
            "SEM-STRUC": {} | string,
            "OUTPUT-SYNTAX"?: string,
            "MEANING-PROCEDURES"?: Array<any>,
            "EXAMPLE-BINDINGS"?: Array<any>,
            "EXAMPLE-DEPS"?: Array<any>,
            "SYNONYMS"?: Array<any>,
            "HYPONYMS"?: string
        }
    }
}
