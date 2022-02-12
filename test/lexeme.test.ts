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
        }
    }
}

test("Adding empty lexeme", () => {
    const o = new Ontoagent()

    o.addLexeme("EMPTY-LEXEME")

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"]
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding empty lexical sense", () => {
    const o = new Ontoagent()

    o.addLexicalSense("EMPTY-LEXEME", {})

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with cat", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-CAT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/category", "N"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with empty sync-struc", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-EMPTY-SYNSTRUC"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with category", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-CAT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/category", "N"],
        [3, "syntactic-structure/id", 2],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with type", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-TYPE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
        [3, "syntactic-structure/type", "PRO"],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with root word", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-ROOTWORD"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
        [3, "syntactic-structure/root-word", 4],
        [3, "syntactic-structure/root-word", 5],
        [4, "lexeme", "STOP"],
        [5, "lexeme", "TURN"],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with root", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-ROOT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
        [3, "syntactic-structure/root", 4],
        [4, "variable", "$VAR0"],
    ]
    // TODO vars should not be global, but attached to a lexical sense

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with tense", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-TENSE"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
        [3, "syntactic-structure/tense", "INFINITIVE"],
        [3, "syntactic-structure/tense", "PROGRESSIVE"],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with number", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-NUMBER"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
        [3, "syntactic-structure/number", "SING"],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with optional", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", lexeme["TEST"]["WITH-SYNSTRUC-W-OPTIONAL"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
        [3, "syntactic-structure/optional", 1],
    ]

    expect(o.query()).toStrictEqual(result)
})
