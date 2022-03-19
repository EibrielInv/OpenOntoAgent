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
                {"ART": [
                        {"ROOT": "$VAR0"},
                        {"CAT": "ART"}
                    ]
                },
                {"ROOT": "$VAR1"},
                {"CAT": "N"},
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
    },
    "DESTINATION": {
        "DESTINATION-N601": {
            "CAT": "N",
            "DEF": "DRIVING DOMAIN",
            "EX": "YOUR DESTINATION IS ON THE RIGHT.",
            "COMMENTS": "",
            "SYN-STRUC": [
                {"USE-EXAMPLE-BINDING": "T"},
                {"DET": [
                        {"ROOT": "$VAR1"},
                        {"ROOT-WORD": "YOUR"},
                        {"CAT": "DET"}
                    ]
                },
                {"ROOT": "$VAR0"},
                {"CAT": "N"},
                {"V": [
                        {"ROOT": "$VAR2"},
                        {"ROOT-WORD": "*BE*"},
                        {"CAT": "V"}
                    ]
                },
                {"PREP": [
                        {"ROOT": "$VAR3"},
                        {"ROOT-WORD": "ON"},
                        {"CAT": "PREP"}
                    ]
                },
                {"ART": [
                        {"ROOT": "$VAR4"},
                        {"ROOT-WORD": "THE"},
                        {"CAT": "ART"}
                    ]
                },
                {"ADJ": [
                        {"ROOT": "$VAR5"},
                        {"ROOT-WORD": "RIGHT"},
                        {"CAT": "ADJ"}
                    ]
                },
            ],
            "SEM-STRUC": {
                "PLACE": {"DESTINATION-OF": {"VALUE": "REFSEM1"}, "SIDE-RL": "RIGHT"},
                "REFSEM1": {
                    "DRIVE": {
                        "AGENT": {"VALUE": "*HEARER*"},
                        "SCOPE-OF": {"VALUE": "REFSEM2"},
                    }
                },
                "REFSEM2": {"MODALITY": {"TYPE": "VOLATIVE", "VALUE": 1}},
            },
            "EXAMPLE-BINDINGS": [
                "YOUR-1",
                "DESTINATION-0",
                "IS-2",
                "ON-3",
                "THE-4",
                "RIGHT-5",
            ],
        },
    }
}

test("Adding A-ART1 lexical sense", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("A", lexicon["A"]["A-ART1"])

    const result: any = [
        [3,"syntactic-structure/object",4],
        [4,"syntactic-structure/category","ART"],
        [2,"sense/category","ART"],
        [4,"syntactic-structure/id",2],
        [1,"lexeme","A"],
        [2,"sense/lexeme",1],
        [2,"sense/syntactic-structure",4],
        [3,"syntactic-structure/category","N"],
        [3,"syntactic-structure/root",6],
        [5,"variable/name","$VAR0"],
        [6,"variable/sense.ref",2],
        [4,"syntactic-structure/root",5],
        [6,"variable/name","$VAR1"],
        [3,"syntactic-structure/id",1],
        [5,"variable/sense.ref",2],
    ]

    expect(o.query()).toBeSameDB(result)

})

test("Adding DESTINATION-N601 lexical sense", () => {
    const o = new Ontoagent()

    o.lexeme.addLexicalSense("DESTINATION", lexicon["DESTINATION"]["DESTINATION-N601"])

    const result: any = [
        [1,"lexeme","DESTINATION"],

        [2,"sense/lexeme",1],
        [2,"sense/category","N"],
        [2,"sense/syntactic-structure",17],
        [2,"sense/semantic-structure",20],

        [3,"syntactic-structure/value","T"],
        [3,"syntactic-structure/object",4],
        [3,"syntactic-structure/object",11],
        [3,"syntactic-structure/root",7],
        [3,"syntactic-structure/object",17],
        [3,"syntactic-structure/object",14],
        [3,"syntactic-structure/category","N"],

        [4,"syntactic-structure/root-word",6],
        [4,"syntactic-structure/category","DET"],
        [4,"syntactic-structure/id",2],


        [5,"variable/name","$VAR1"],

        [6,"lexeme","YOUR"],

        [7,"variable/sense.ref",2],
        [7,"variable/name","$VAR0"],

        [8,"syntactic-structure/id",3],
        [8,"syntactic-structure/category","V"],

        [9,"variable/name","$VAR2"],

        [30,"semantic-structure.concept.property/value","REFSEM2"],
        [18,"variable/sense.ref",2],
        [30,"semantic-structure.concept.property/name","VALUE"],
        [11,"syntactic-structure/category","PREP"],
        [27,"semantic-structure.concept.property/name","AGENT"],
        [15,"variable/sense.ref",2],
        [23,"semantic-structure.concept.property/name","VALUE"],
        [27,"semantic-structure.concept.property/property",28],
        [33,"semantic-structure.concept.property/name","TYPE"],
        [12,"variable/sense.ref",2],
        [28,"semantic-structure.concept.property/name","VALUE"],
        [15,"variable/name","$VAR4"],
        [11,"syntactic-structure/id",4],
        [17,"syntactic-structure/root-word",19],
        [20,"semantic-structure.concept.property/property",31],
        [13,"lexeme","ON"],
        [26,"semantic-structure.concept.property/property",27],
        [14,"syntactic-structure/category","ART"],
        [18,"variable/name","$VAR5"],
        [17,"syntactic-structure/id",6],
        [21,"semantic-structure.concept.property/name","PLACE"],
        [25,"semantic-structure.concept.property/name","REFSEM1"],
        [11,"syntactic-structure/root",12],
        [25,"semantic-structure.concept.property/property",26],
        [28,"semantic-structure.concept.property/value","*HEARER*"],
        [11,"syntactic-structure/root-word",13],
        [29,"semantic-structure.concept.property/name","SCOPE-OF"],
        [26,"semantic-structure.concept.property/name","DRIVE"],
        [32,"semantic-structure.concept.property/property",34],
        [21,"semantic-structure.concept.property/property",22],
        [23,"semantic-structure.concept.property/value","REFSEM1"],
        [31,"semantic-structure.concept.property/name","REFSEM2"],
        [12,"variable/name","$VAR3"],
        [29,"semantic-structure.concept.property/property",30],
        [32,"semantic-structure.concept.property/property",33],
        [10,"lexeme","*BE*"],
        [31,"semantic-structure.concept.property/property",32],
        [9,"variable/sense.ref",2],
        [20,"semantic-structure.concept.property/property",21],
        [22,"semantic-structure.concept.property/name","DESTINATION-OF"],
        [17,"syntactic-structure/root",18],
        [16,"lexeme","THE"],
        [14,"syntactic-structure/id",5],
        [8,"syntactic-structure/root-word",10],
        [19,"lexeme","RIGHT"],
        [33,"semantic-structure.concept.property/value","VOLATIVE"],
        [14,"syntactic-structure/root",15],
        [4,"syntactic-structure/root",5],
        [24,"semantic-structure.concept.property/name","SIDE-RL"],
        [26,"semantic-structure.concept.property/property",29],
        [3,"syntactic-structure/object",8],
        [22,"semantic-structure.concept.property/property",23],
        [21,"semantic-structure.concept.property/property",24],
        [34,"semantic-structure.concept.property/name","VALUE"],
        [32,"semantic-structure.concept.property/name","MODALITY"],
        [20,"semantic-structure/id",1],
        [3,"syntactic-structure/id",1],
        [24,"semantic-structure.concept.property/value","RIGHT"],
        [8,"syntactic-structure/root",9],
        [20,"semantic-structure.concept.property/property",25],
        [17,"syntactic-structure/category","ADJ"],
        [14,"syntactic-structure/root-word",16],
        [5,"variable/sense.ref",2]
    ]

    expect(o.query()).toBeSameDB(result)

})
