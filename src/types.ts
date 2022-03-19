
export interface ConceptPropertiesDB {
    [key: string]: string|Array<string>
}

export interface ConceptDB {
    [key: string]: ConceptPropertiesDB | string
}

export interface OntologyDB {
    [key: string]: ConceptDB
}
