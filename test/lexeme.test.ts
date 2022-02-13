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
                {"NAME": "CAT", "VALUE": "N"}
            ]
        },
        "WITH-SYNSTRUC-W-ROOT": {
            "SYN-STRUC": [
                {"NAME": "ROOT", "VALUE": "$VAR0"}
            ]
        },
        "WITH-SYNSTRUC-W-TYPE": {
            "SYN-STRUC": [
                {"NAME": "TYPE", "VALUE": "PRO"}
            ]
        },
        "WITH-SYNSTRUC-W-ROOTWORD": {
            "SYN-STRUC": [
                {"NAME": "ROOT-WORD", "VALUE": ["STOP", "TURN"]}
            ]
        },
        "WITH-SYNSTRUC-W-TENSE": {
            "SYN-STRUC": [
                {"NAME": "TENSE", "VALUE": ["INFINITIVE", "PROGRESSIVE"]}
            ]
        },
        "WITH-SYNSTRUC-W-NUMBER": {
            "SYN-STRUC": [
                {"NAME": "NUMBER", "VALUE": "SING"}
            ]
        },
        "WITH-SYNSTRUC-W-OPTIONAL": {
            "SYN-STRUC": [
                {"NAME": "OPT", "VALUE": "+"}
            ]
        },
        //
        "WITH-SYNSTRUC-W-MULTIPLE": {
            "SYN-STRUC": [
                {"NAME": "ROOT", "VALUE": "$VAR1"},
                {"NAME": "CAT", "VALUE": "N"},
            ]
        },
        "WITH-SYNSTRUC-W-HIERARCHICAL": {
            "SYN-STRUC": [
                {"NAME": "ART", "VALUE": [
                        {"NAME": "ROOT", "VALUE": "$VAR0"},
                        {"NAME": "CAT", "VALUE": "ART"}
                    ]
                },
            ]
        },
        "WITH-SYNSTRUC-W-VAR": {
            "SYN-STRUC": [
                {"NAME": "ROOT", "VALUE": "$VAR1"}
            ]
        }
    }
}

test("Adding empty lexeme", () => {
    const o = new Ontoagent()

    o.addLexeme("EMPTY-LEXEME")

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"]
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding empty lexical sense", () => {
    const o = new Ontoagent()

    o.addLexicalSense("EMPTY-LEXEME", {})

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with cat", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-CAT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/category", "N"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with empty sync-struc", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-EMPTY-SYNSTRUC"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 1],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with category", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-CAT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/category", "N"],
        [3, "syntactic-structure/id", 1],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with type", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-TYPE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/type", "PRO"],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with root word", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-ROOTWORD"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/root-word", 4],
        [3, "syntactic-structure/root-word", 5],
        [4, "lexeme", "STOP"],
        [5, "lexeme", "TURN"],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with root", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-ROOT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/root", 4],
        [4, "variable/name", "$VAR0"],
        [4, "variable/sense.ref", 2],
    ]
    // TODO vars should not be global, but attached to a lexical sense

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with tense", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-TENSE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/tense", "INFINITIVE"],
        [3, "syntactic-structure/tense", "PROGRESSIVE"],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with number", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-NUMBER"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/number", "SING"],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with optional", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-OPTIONAL"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/optional", 1],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with multiple elements", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-MULTIPLE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/category", "N"],
        [3, "syntactic-structure/id", 1],
        [3, "syntactic-structure/root", 4],
        [4, "variable/name", "$VAR1"],
        [4, "variable/sense.ref", 2],
    ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with hierarchical elements", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-HIERARCHICAL"])

    const result = [
        [ 1, 'lexeme', 'TEST' ],
        [ 2, 'sense/lexeme', 1 ],
        [ 3, 'syntactic-structure/id', 1 ],
        [ 3, 'syntactic-structure/object', 4 ],
        [ 4, 'syntactic-structure/id', 2 ],
        [ 4, 'syntactic-structure/category', 'ART' ],
        [ 4, 'syntactic-structure/root', 5 ],
        [ 5, 'variable/name', '$VAR0' ],
        [ 5, 'variable/sense.ref', 2 ]
      ]

    expect(o.query()).toEqual(expect.objectContaining(result))
})

test("Adding lexical sense with sync-struc with 2 vars", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-VAR"])
    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-VAR"])

    const result = [
        [ 1, 'lexeme', 'TEST' ],
        [ 2, 'sense/lexeme', 1 ],
        [ 3, 'syntactic-structure/id', 1 ],
        [ 3, 'syntactic-structure/root', 4 ],
        [ 4, 'variable/name', '$VAR1' ],
        [ 4, 'variable/sense.ref', 2 ],
        [ 5, 'sense/lexeme', 1 ],
        [ 6, 'syntactic-structure/root', 7 ],
        [ 6, 'syntactic-structure/id', 2 ],
        [ 7, 'variable/name', '$VAR1' ],
        [ 7, 'variable/sense.ref', 5 ],
      ]


    //expect(o.query()).toStrictEqual(result)
    expect(o.query()).toEqual(expect.objectContaining(result))
})
