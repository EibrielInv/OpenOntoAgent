import {Ontoagent} from "../src/index"

const lexeme: any = {
    "SEM": {
        "SEM1": {
            "SEM-STRUC": "SQUIRREL",
        },
        "SEM2": {
            "SEM-STRUC": {
                "INGEST": {
                    "AGENT": {
                        "VALUE": "^$VAR1"
                    },
                    "THEME": {
                        "VALUE": "^$VAR2"
                    }
                }
            },
        }
    }
}

test("Adding lexical sense with simple sem-struc", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("SEM", lexeme["SEM"]["SEM1"])

    const result = [
        [1, "lexeme", "SEM"],
        [2, "sense/lexeme", 1],
        [2, "sense/semantic-structure", 3],
        [3, "semantic-structure/id", 1],
        [3, "semantic-structure.concept.property/property", 4],
        [4, "semantic-structure.concept.property/name", "SQUIRREL"]
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with complex sem-struc", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("SEM", lexeme["SEM"]["SEM2"])

    const result = [
        [1, "lexeme", "SEM"],

        [2, "sense/lexeme", 1],
        [2, "sense/semantic-structure", 3],

        [3, "semantic-structure/id", 1],
        [3, "semantic-structure.concept.property/property", 4],

        [4, "semantic-structure.concept.property/name", "INGEST"],
        [4, "semantic-structure.concept.property/property", 5],
        [4, "semantic-structure.concept.property/property", 7],

        [5, "semantic-structure.concept.property/name", "AGENT"],
        [5, "semantic-structure.concept.property/property", 6],

        [6, "semantic-structure.concept.property/name", "VALUE"],
        [6, "semantic-structure.concept.property/value", "^$VAR1"],

        [7, "semantic-structure.concept.property/property", 8],
        [7, "semantic-structure.concept.property/name", "THEME"],

        [8, "semantic-structure.concept.property/name", "VALUE"],
        [8, "semantic-structure.concept.property/value", "^$VAR2"],
    ]

    expect(o.query()).toBeSameDB(result)
})
