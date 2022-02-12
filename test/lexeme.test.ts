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
            "SYN-STRUC": {}
        },
        "WITH-SYNSTRUC-W-CAT": {
            "SYN-STRUC": {
                "CAT": "N"
            }
        },
        "WITH-SYNSTRUC-W-ROOT": {
            "SYN-STRUC": {
                "ROOT": "$VAR0"
            }
        },
        "WITH-SYNSTRUC-W-TYPE": {
            "SYN-STRUC": {
                "TYPE": "PRO"
            }
        },
        "WITH-SYNSTRUC-W-ROOTWORD": {
            "SYN-STRUC": {
                "ROOT-WORD": ["STOP", "TURN"]
            }
        }
    }
}


test("Adding empty lexeme", () => {
    const o = new Ontoagent()

    o.addLexeme("EMPTY-LEXEME", {})

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"]
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding empty lexical sense", () => {
    const o = new Ontoagent()

    o.addLexicalSense("EMPTY-LEXEME", "EMPTY-LEXICAL-SENSE", {})

    const result = [
        [1, "lexeme", "EMPTY-LEXEME"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with cat", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", "WITH-CAT", lexeme["TEST"]["WITH-CAT"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/category", "N"],
        [2, "sense/lexeme", 1],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with empty sync-struc", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", "WITH-EMPTY-SYNSTRUC", lexeme["TEST"]["WITH-EMPTY-SYNSTRUC"])

    const result = [
        [1, "lexeme", "TEST"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/id", 2],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding lexical sense with sync-struc with category", () => {
    const o = new Ontoagent()

    o.addLexicalSense("TEST", "WITH-SYNSTRUC-W-CAT", lexeme["TEST"]["WITH-SYNSTRUC-W-CAT"])

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

    o.addLexicalSense("TEST", "WITH-SYNSTRUC-W-TYPE", lexeme["TEST"]["WITH-SYNSTRUC-W-TYPE"])

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

    o.addLexicalSense("TEST", "WITH-SYNSTRUC-W-ROOTWORD", lexeme["TEST"]["WITH-SYNSTRUC-W-ROOTWORD"])

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
