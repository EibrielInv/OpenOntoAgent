import {Ontoagent} from "../src/index"

const lexeme: any = {
    "SQUIRREL": {
        "SQUIRREL-N1": {
            "CAT": "N",
            "SYN-STRUC": {
                "ROOT": "$VAR0",
                "CAT": "N"
            },
            "SEM-STRUC": "SQUIRREL",
        }
    },
    "TEST": {
        "WITH-CAT": {
            "CAT": "N"
        },
        "WITH-EMPTY-SYNSTRUC": {
            "SYN-STRUC": []
        },
        "WITH-SYNSTRUC-W-CAT": {
            "SYN-STRUC": [
                {"CAT": "N"}
            ]
        },
        "WITH-SYNSTRUC-W-ROOT": {
            "SYN-STRUC": [
                {"ROOT": "$VAR0"}
            ]
        },
        "WITH-SYNSTRUC-W-TYPE": {
            "SYN-STRUC": [
                {"TYPE": "PRO"}
            ]
        },
        "WITH-SYNSTRUC-W-ROOTWORD": {
            "SYN-STRUC": [
                {"ROOT-WORD": ["STOP", "TURN"]}
            ]
        },
        "WITH-SYNSTRUC-W-TENSE": {
            "SYN-STRUC": [
                {"TENSE": ["INFINITIVE", "PROGRESSIVE"]}
            ]
        },
        "WITH-SYNSTRUC-W-NUMBER": {
            "SYN-STRUC": [
                {"NUMBER": "SING"}
            ]
        },
        "WITH-SYNSTRUC-W-OPTIONAL": {
            "SYN-STRUC": [
                {"OPT": "+"}
            ]
        },
        //
        "WITH-SYNSTRUC-W-MULTIPLE": {
            "SYN-STRUC": [
                {"ROOT": "$VAR1"},
                {"CAT": "N"},
            ]
        },
        "WITH-SYNSTRUC-W-HIERARCHICAL": {
            "SYN-STRUC": [
                {"ART": [
                        {"ROOT": "$VAR0"},
                        {"CAT": "ART"}
                    ]
                },
            ]
        },
        "WITH-SYNSTRUC-W-VAR": {
            "SYN-STRUC": [
                {"ROOT": "$VAR1"}
            ]
        }
    }
}

test("Adding empty lexeme", () => {
    const o = new Ontoagent()

    o.lexeme.addLexeme("EMPTY-LEXEME")

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"]
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding empty lexical sense", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("EMPTY-LEXEME", {})

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with cat", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-CAT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/category", "N"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with empty sync-struc", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-EMPTY-SYNSTRUC"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/id", 1],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with category", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-CAT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/category", "N"],
        [3, "syntactic-structure/id", 1],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with type", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-TYPE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/type", "PRO"],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with root word", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-ROOTWORD"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/root-word", 4],
        [3, "syntactic-structure/root-word", 5],
        [4, "lexeme", "STOP"],
        [5, "lexeme", "TURN"],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with root", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-ROOT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/root", 4],
        [4, "variable/name", "$VAR0"],
        [4, "variable/sense.ref", 2],
    ]
    // TODO vars should not be global, but attached to a lexical sense

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with tense", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-TENSE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/tense", "INFINITIVE"],
        [3, "syntactic-structure/tense", "PROGRESSIVE"],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with number", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-NUMBER"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/number", "SING"],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with optional", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-OPTIONAL"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/optional", 1],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with multiple elements", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-MULTIPLE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [2, "sense/syntactic-structure", 3],
        [3, "syntactic-structure/category", "N"],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/root", 4],
        [4, "variable/name", "$VAR1"],
        [4, "variable/sense.ref", 2],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with hierarchical elements", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-HIERARCHICAL"])

    const result = [
        [1, 'lexeme', 'TEST'],
        [2, 'sense/lexeme', 1],
        [2, "sense/syntactic-structure", 4],
        [3, 'syntactic-structure/id', 1],
        [3, 'syntactic-structure/object', 4],
        [4, 'syntactic-structure/id', 2],
        [4, 'syntactic-structure/category', 'ART'],
        [4, 'syntactic-structure/root', 5],
        [5, 'variable/name', '$VAR0'],
        [5, 'variable/sense.ref', 2]
      ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding lexical sense with sync-struc with 2 vars", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-VAR"])
    o.lexeme.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-VAR"])

    const result = [
        [1, 'lexeme', 'TEST'],
        [2, 'sense/lexeme', 1],
        [2, "sense/syntactic-structure", 3],
        [3, 'syntactic-structure/id', 1],
        [3, 'syntactic-structure/root', 4],
        [4, 'variable/name', '$VAR1'],
        [4, 'variable/sense.ref', 2],
        [5, 'sense/lexeme', 1],
        [5, "sense/syntactic-structure", 6],
        [6, 'syntactic-structure/root', 7],
        [6, 'syntactic-structure/id', 2],
        [7, 'variable/name', '$VAR1'],
        [7, 'variable/sense.ref', 5],
      ]


    expect(o.query()).toBeSameDB(result)
})
