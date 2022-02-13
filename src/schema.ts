export var schema = {
    // Concepts
    "concept/name": {
        //":db/valueType": ":db.type/string",
        //":db/unique": ":db.unique/identity"
    },
    "concept/is-a": {
        ":db/valueType": ":db.type/ref"
    },
    "concept/property": {
        ":db/valueType": ":db.type/ref",
        ":db/cardinality": ":db.cardinality/many"
    },

    // Concept property
    "concept.property/name": {
        //":db/valueType": ":db.type/string",
        ":db/cardinality": ":db.cardinality/one"
    },
    "concept.property/default": {
        ":db/valueType": ":db.type/ref", // concept
        ":db/cardinality": ":db.cardinality/one"
    },
    "concept.property/semantic": {
        ":db/valueType": ":db.type/ref", // concepts
        ":db/cardinality": ":db.cardinality/many"
    },
    "concept.property/relaxable-to": {
        ":db/valueType": ":db.type/ref", // concepts
        ":db/cardinality": ":db.cardinality/many"
    },
    "concept.property/not": {
        ":db/valueType": ":db.type/ref", // concepts
        ":db/cardinality": ":db.cardinality/many"
    },

    // Lexeme
    "lexeme": {
        //":db/valueType": ":db.type/string",
        ":db/unique": ":db.unique/identity"
    },

    // Lexical sense
    "sense/lexeme": {
        ":db/valueType": ":db.type/ref", // lexeme/string
        ":db/cardinality": ":db.cardinality/one"
    },
    "sense/category": {
        //":db/valueType": ":db.type/string", // category
        ":db/cardinality": ":db.cardinality/one"
    },
    "sense/syntactic-structure": {
        ":db/valueType": ":db.type/ref", // syntactic-structure/id
        ":db/cardinality": ":db.cardinality/one"
    },
    "sense/semantic-structure": {
        ":db/valueType": ":db.type/ref", // concept
        ":db/cardinality": ":db.cardinality/one"
    },

    // Syntactic Structure
    "syntactic-structure/id": {
        //":db/valueType": ":db.type/ref", // lexeme/string   . Or UUID?
        ":db/cardinality": ":db.cardinality/one"
    },
    "syntactic-structure/root": {
        ":db/valueType": ":db.type/ref", // pointer
        ":db/cardinality": ":db.cardinality/one"
    },
    "syntactic-structure/category": {
        //":db/valueType": ":db.type/string", // category
        ":db/cardinality": ":db.cardinality/many"
    },
    "syntactic-structure/type": {
        //":db/valueType": ":db.type/string", // type
        ":db/cardinality": ":db.cardinality/many"
    },
    "syntactic-structure/root-word": {
        ":db/valueType": ":db.type/ref", // lexeme or lexical-sense
        ":db/cardinality": ":db.cardinality/many"
    },
    "syntactic-structure/tense": {
        //":db/valueType": ":db.type/string", // tense
        ":db/cardinality": ":db.cardinality/many"
    },
    "syntactic-structure/number": {
        //":db/valueType": ":db.type/string", // number (singular, plural)
        ":db/cardinality": ":db.cardinality/many"
    },
    "syntactic-structure/optional": {
        //":db/valueType": ":db.type/boolean", // optional
        ":db/cardinality": ":db.cardinality/one"
    },
    "syntactic-structure/next": {
        ":db/valueType": ":db.type/ref", // syntactic-structure
        ":db/cardinality": ":db.cardinality/one"
    },
    "syntactic-structure/object": {
        ":db/valueType": ":db.type/ref", // syntactic-structure
        ":db/cardinality": ":db.cardinality/many"
    },


    // Semantic Structure
    "semantic-structure/id": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "semantic-structure/concept": {
        ":db/valueType": ":db.type/ref", // semantic-structure concept to match
        ":db/cardinality": ":db.cardinality/many"
    },
    "semantic-structure.concept/name": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "semantic-structure.concept/property": {
        ":db/valueType": ":db.type/ref", // semantic-structure concept property to match
        ":db/cardinality": ":db.cardinality/many"
    },
    "semantic-structure.concept.property/name": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "semantic-structure.concept.property/value": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "semantic-structure.concept.property/property": {
        ":db/valueType": ":db.type/ref", // semantic-structure concept property property to match
        ":db/cardinality": ":db.cardinality/many"
    },


    // Variable
    "variable/name": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "variable/sense.ref": {
        ":db/valueType": ":db.type/ref", // lexical-sense
        ":db/cardinality": ":db.cardinality/one"
    },

    // Tmr
    "tmr/sentence": {
        //":db/valueType": ":db.type/string",
        ":db/cardinality": ":db.cardinality/one"
    },
    "tmr/element": {
        ":db/valueType": ":db.type/ref",
        ":db/cardinality": ":db.cardinality/many"
    },
}
