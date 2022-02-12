
export {
    tmr,
    ontology,
    lexicon
}

/*
INGEST-1
    AGENT     SQUIRREL-1
    THEME     NUT-FOODSTUFF-1
    TIME      find-anchor-time
SQUIRREL-1
    COLOR     BROWN
    AGENT-OF  INGEST-1
NUT-FOODSTUFF-1
    THEME-OF  INGEST-1
*/


const tmr = {
    "OriginalSentence": "A Brown Squirrel Is Eating a Nut",
    "TMR": {

        "INGEST-1": {
            "AGENT": "SQUIRREL-1",
            "THEME": "NUT-FOODSTUFF-1",
            'TIME': ['FIND-ANCHOR-TIME'],
            "CONCEPT": "INGEST",

            // "from-sense": "EAT-V1"
        },

        "SQUIRREL-1": {
            "COLOR": "BROWN",
            "AGENT-OF": "INGEST-1",
            "CONCEPT": "SQUIRREL",

            // "from-sense": "SQUIRREL-V1"
        },

        "NUT-FOODSTUFF-1": {
            "THEME-OF": "INGEST-1",
            "CONCEPT": "NUT-FOODSTUFF",

            // "from-sense": "NUT-V1"
        }
    }
}


/*
eat-v1: “ingest,” as in “He was eating (cheese).”

syn-struc
  subject  $var1
  root  $var0
  directobject $var2 (optional)

sem-struc
  INGEST
    AGENT  ^$var1
    THEME  ^$var2
*/

const lexicon = {
    "A": {
        "A-ART1": {
            "CAT": "ART",
            "DEF": "indicates no coreference",
            "EX": "A cat walked in the room",
            "COMMENTS": "",
            "TMR-HEAD": "$VAR1",
            "SYN-STRUC": {
                "ART": {"ROOT": "$VAR0", "CAT": "ART"},
                "ROOT": "$VAR1",
                "CAT": "N",
            },
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

    "IS": {
        "IS-A2": {
            "CAT": "AUX",
            "DEF": "",
            "EX": "She is sick",
            "COMMENTS": "",
            "TMR-HEAD": "NIL",
            "SYN-STRUC": {
                "SUBJECT": {
                    "ROOT": "$VAR1",
                    "CAT": "N"
                },
                "ROOT": "$VAR0",
                "CAT": "AUX",
                "V": {
                    "ROOT": "$VAR2",
                    "CAT": "V"
                }
            },
            "SEM-STRUC": ""
        }
    },

    "EAT": {
        "EAT-V1": {
            "CAT": "V",
            "SYN-STRUC": {
                "SUBJECT": {
                    "ROOT": "$VAR1",
                    "CAT": "N"
                },
                "ROOT": "$VAR0",
                "CAT": "V",
                "DIRECTOBJECT": {
                    "ROOT": "$VAR2",
                    "CAT": "N",
                    "OPT": "+"
                },
            },
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
    },

    "NUT": {
        "NUT-FOODSTUFF-N1": {
            "CAT": "N",
            "SYN-STRUC": {
                "ROOT": "$VAR0",
                "CAT": "N"
            },
            "SEM-STRUC": "NUT-FOODSTUFF"
        }
    }
}

/*
INGEST
  AGENT
    sem ANIMAL
    relaxable-to SOCIAL-OBJECT
  THEME
    sem FOOD , BEVERAGE , INGESTIBLE-MEDICATION
    relaxable-to ANIMAL , PLANT
    not HUMAN

*/

const ontology = {
    "INGEST": {
        "AGENT": {
            "SEM": "ANIMAL",
            "RELAXABLE-TO": ["SOCIAL-OBJECT"]
        },
        "THEME": {
            "SEM": ["FOOD", "BEVERAGE", "INGESTIBLE-MEDICATION"],
            "RELAXABLE-TO": ["ANIMAL", "PLANT"],
            "NOT": "HUMAN"
        }
    },

    "NUT-FOODSTUFF": {
        "IS-A": "FOOD"
    },

    "FOOD": {
        "IS-A": "SOLID"
    },

    "SQUIRREL": {
        "IS-A": "ANIMAL"
    },

    "ANIMAL": {
        "IS-A": "ORGANISM"
    }
}
