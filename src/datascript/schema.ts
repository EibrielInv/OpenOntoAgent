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

    // Tmr
    "tmr/id": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "tmr/instance": {
        ":db/valueType": ":db.type/ref",
        ":db/cardinality": ":db.cardinality/many"
    },
    "tmr/sentence": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "tmr/element": {
        ":db/valueType": ":db.type/ref",
        ":db/cardinality": ":db.cardinality/many"
    },
    "tmr.instance/id": {
        ":db/cardinality": ":db.cardinality/one"
    },

    // Tmr Property
    "tmr.instance.property/property": {
        ":db/valueType": ":db.type/ref", // semantic-structure concept property to match
        ":db/cardinality": ":db.cardinality/many"
    },
    "tmr.instance.property/name": {
        ":db/cardinality": ":db.cardinality/one"
    },
    "tmr.instance.property/value": {
        ":db/cardinality": ":db.cardinality/one"
    }
}
