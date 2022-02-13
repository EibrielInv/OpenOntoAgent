import {Ontoagent} from "../src/index"


const lexicon: any = {
    "A": {
        "A-ART1": {
            "CAT": "ART",
            "DEF": "indicates no coreference",
            "EX": "A cat walked in the room",
            "COMMENTS": "",
            "TMR-HEAD": "$VAR1",
            "SYN-STRUC": [
                {"NAME": "ART", "VALUE": [
                    {"NAME": "ROOT", "VALUE": "$VAR0"},
                    {"NAME": "CAT", "VALUE": "ART"}
                ]},
                {"NAME": "ROOT", "VALUE": "$VAR1"},
                {"NAME": "CAT", "VALUE": "N"},
            ],
            "SEM-STRUC": "",
            "OUTPUT-SYNTAX": "NP",
            "MEANING-PROCEDURES": [
                ["BLOCK-REFERENCE", ["TARGET", "^$VAR1"], ["DETERMINATE", "NO"]]
            ],
            "EXAMPLE-BINDINGS": ["YOU", "HAVE", "A-0", "DOG-1"],
            "EXAMPLE-DEPS": [["DET", "$VAR1", "$VAR0"]],
            "SYNONYMS": ["AN"],
            "HYPONYMS": "NIL",
        }
    }
}

test("Adding A-ART1 lexical sense", () => {
    const o = new Ontoagent()

    o.addLexicalSense("A", lexicon["A"]["A-ART1"])

    const result: any = [
        [3, "syntactic-structure/object", 4],
        [4, "syntactic-structure/category", "ART"],
        [2, "sense/category", "ART"],
        [4, "syntactic-structure/id", 2],
        [2, "sense/syntactic-structure", 4],
        [1, "lexeme", "A"],
        [2, "sense/lexeme", 1],
        [3, "syntactic-structure/category", "N"],
        [3, "syntactic-structure/root", 6],
        [5, "variable/name", "$VAR0"],
        [6, "variable/sense.ref", 2],
        [4, "syntactic-structure/root", 5],
        [6, "variable/name", "$VAR1"],
        [3, "syntactic-structure/id", 1],
        [5, "variable/sense.ref", 2]
    ]

    expect(o.query()).toBeSameDB(result)

})
