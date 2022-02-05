
eat_v1 = {
    "DEFINITION": "ingest",
    "EXAMPLE": "He was eating (cheese).",

    "SYNTACTIC-STRUCTURE": [
        {
            "SUBJECT": "$VAR1",
            "V": "$VAR0",
            "DIRECTOBJECT": "$VAR2(opt+)"  # OPTIONAL
        }
    ],

    "SEMANTIC-STRUCTURE": {
        "INGEST": {
            "AGENT": "^$VAR1",  # ^ -> the meaning of
            "BENEFICIARY": "^$VAR2(sem FOOD)"  # ^ -> the meaning of
        }
    },
}

eat_v2 = {
    "DEFINITION": "The construction ‘eat away at’: erode physically",
    "EXAMPLE": "The rust ate away at the pipe.",

    "SYNTACTIC-STRUCTURE": [
        {
            "SUBJECT": "$VAR1",
            "V": "$VAR0",
            "ADV": "$VAR2(root'away')",
            "PP": {
                "PREP": "$VAR3(root'at')",
                "OBJ": "$VAR4"
            }
        }
    ],

    "SEMANTIC-STRUCTURE": {
        "ERODE": {
            "INSTRUMENT": "^$VAR1",
            "THEME": "^$VAR4"
        },
        "$VAR2": "null-sem+",  # null-sem+: meaning has already been taken care of
        "$VAR3": "null-sem+"
    }
}


# sd

see_v1 = {
    "SEE-V1": {
        "DEFINITION": "to perceive visually",
        "EXAMPLE": "He saw her new car.",

        "SYNTACTIC-STRUCTURE": [
            {
                "SUBJECT": "$VAR1",
                "V": "$VAR0",
                "DIRECTOBJECT": "$VAR2"
            }
        ]
    },

    "SEMANTIC-STRUCTURE": {
        "INVOLUNTARY-VISUAL-EVENT": {
            "AGENT": "^$VAR1(sem ANIMAL)",
            "THEME": "^$VAR2(sem PHYSICAL-OBJECT)"
        }
    }
}

see_v2 = {
    "SEE-V2": {
        "DEFINITION": "to consult with for advice",
        "EXAMPLE": "Grandma saw her doctor.",

        "SYNTACTIC-STRUCTURE": [
            {
                "SUBJECT": "$VAR1",
                "V": "$VAR0",
                "DIRECTOBJECT": "$VAR2"
            }
        ]
    },

    "SEMANTIC-STRUCTURE": {
        "PROFESSIONAL-CONSULTATION": {
            "AGENT": "^$VAR2(sem MEDICAL-ROLE,LEGAL-ROLE)",
            "BENEFICIARY": "^$VAR1(sem HUMAN)"
        }
    }
}

see_v3 = {
    "SEE-V3": {
        "DEFINITION": "to refer to a portion of text",
        "EXAMPLE": "For details, see chapter 3.",

        "SYNTACTIC-STRUCTURE": [
            {
                "V": "$VAR0(form imperative)",
                "DIRECTOBJECT": "$VAR1"
            }
        ]
    },

    "SEMANTIC-STRUCTURE": {
        "READ": {
            "THEME": "^$VAR1(sem TEXT-UNIT)"
        }
    }
}

see_v4 = {
    "SEE-V4": {
        "DEFINITION": "to accompany someone somewhere",
        "EXAMPLE": "He saw me to my car.",

        "SYNTACTIC-STRUCTURE": [
            {
                "SUBJECT": "$VAR1",
                "V": "$VAR0",
                "DIRECTOBJECT": "$VAR2",
                "PP": {
                    "PREP": "$VAR3(root'to')",
                    "OBJ": "$VAR4"
                }
            }
        ],

        "SEMANTIC-STRUCTURE": {
            "SCORT": {
                "AGENT": "^$VAR1(sem HUMAN)",
                "BENEFICIARY": "^$VAR2(sem HUMAN)",
                "DESTINATION": "^$VAR2(sem PLACE)(relaxable-to PHYSICAL-OBJECT)"
            },
            "$VAR3": "null-sem+"
        }
    }
}

#
address_v1 = {
    "ADDRESS-V1": {
        "CATEGORY": "V",
        "DEFINITION": "to talk to - usually formally",
        "EXAMPLE": "He addressed the audience.",
        "COMMENTS": "",

        "TMR-HEAD": null,

        "SYNTACTIC-STRUCTURE": [
            [
                {
                    "SUBJECT": [
                        {
                            "ROOT": "$VAR1",
                            "CATEGORY": "N"
                        }
                    ]
                },
                {
                    "ROOT": "$VAR0",
                    "CATEGORY": "V"
                },
                {
                    "DIRECTOBJECT": {
                        "ROOT": "$VAR2",
                        "CATEGORY": "N"
                    }
                }
            ]
        ],

        "SEMANTIC-STRUCTURE": {
            "SPEECH-ACT": {
                "AGENT": {"VALUE": "^$VAR1"},
                "BENEFICIARY": {"VALUE": "^$VAR2"}
            }
        },

        "OUTPUT-SYNTAX": null,
        "MEANING-PROCEDURES": null,
        "EXAMPLE-BINDINGS": "THE MAN-1 ADDRESSED-0 THE CROWD-2",
        "EXAMPLE-DEPS": {
            "DOBJ": ["$VAR0", "$VAR2"],
            "NSUBJ": ["$VAR0", "$VAR1"]
        },

        "SYNONYMS": null,
        "HYPONYMS": null
    }
}


address_v3 = {
    "ADDRESS-V3": {
        "CATEGORY": "V",
        "DEFINITION": "to consider, think about",
        "EXAMPLE": "He addressed the problem.",
        "COMMENTS": "",

        "TMR-HEAD": null,

        "SYNTACTIC-STRUCTURE": [
            [
                {
                    "SUBJECT": [
                        {
                            "ROOT": "$VAR1",
                            "CATEGORY": "N"
                        }
                    ]
                },
                {
                    "ROOT": "$VAR0",
                    "CATEGORY": "V"
                },
                {
                    "DIRECTOBJECT": {
                        "ROOT": "$VAR2",
                        "CATEGORY": "N"
                    }
                }
            ]
        ],

        "SEMANTIC-STRUCTURE": {
            "CONSIDER": {
                "AGENT": {"VALUE": "^$VAR1"},
                "THEME": {
                    "VALUE": "^$VAR2",
                    "SEM": "ABSTRACT-OBJECT"
                }
            }
        },

        "OUTPUT-SYNTAX": null,
        "MEANING-PROCEDURES": null,
        "EXAMPLE-BINDINGS": "THE MAN-1 ADDRESSED-0 THE PROBLEM-2",
        "EXAMPLE-DEPS": {
            "DOBJ": ["$VAR0", "$VAR2"],
            "NSUBJ": ["$VAR0", "$VAR1"]
        },

        "SYNONYMS": null,
        "HYPONYMS": null
    }
}


# Lexeme as concept

# Created from textual description
# Zionist is described as a POLITICAL-­ROLE that is further specified as the AGENT-­OF a
# SUP-PORT event whose THEME is the NATION that HAS-­NAME ‘Israel’.
zionist_n1 = {
    "ZIONIST_N1": {

        "SEMANTIC-STRUCTURE": {

            "POLITICAL-ROLE": {
                "AGENT-OF": "SUPPORT"
            },
            "SUPPORT": {
                "THEME": {
                    "VALUE": "NATION",
                    "HAS-NAME": "Isrel"
                }
            }

        }

    }
}

#
# The verbal sense of asphalt (as in They asphalted our road) is described as a COVER event
# whose INSTRUMENT is ASPHALT and whose THEME is ROADWAY-­ARTIFACT . The ontological
# description of COVER , by contrast, indicates that this concept has much broader applicabil-
# ity, permitting its INSTRUMENT and THEME to be any PHYSICAL-­OBJECT .
asphalt_v1 = {

}

# The verb recall, as used in They recalled the high chairs, is described as a RETURN-­
# OBJECT event that is CAUSED-­BY a REQUEST-­ACTION event whose AGENT is a FOR-­PROFIT-
# CORPORATION and whose THEME is ARTIFACT , INGESTIBLE or MATERIAL . ­Here, too, the
# constraints on CAUSED-­BY and THEME are narrower than are required by the concept
# RETURN-­OBJECT .
recall_v1 = {

}

#
overboard_adv1 = {
    "OVERBOARD-ADV1": {
        "DEFINITION": "indicates that the source of the motion is a boat and the destination is a body of water",
        "EXAMPLE": "They threw the rotten food overboard. He jumped overboard.",

        "SYNTACTIC-STRUCTURE": {
            "ROOT": "$VAR1(cat v)",
            "MODS": "$VAR0"
        },

        "SEMANTIC-STRUCTURE": {
            #  Modifying a MOTION-EVENT
            "^$VAR1(sem MOTION-EVENT)": {
                "SOURCE": "SURFACE-WATER-VEHICLE",
                "DESTINATION": "BODY-OF-WATER"
            }
        }
    }
}

#
rain_v1 = {
    "RAIN-V1": {
        "DEFINITION": "the construction for expressing rain events",
        "EXAMPLE": "It is raining. It rains a lot here. It has just rained.",

        "SYNTACTIC-STRUCTURE": {
            "SUBJECT": "$VAR1(root it)",
            "V": "$VAR0"
        },

        "SEMANTIC-STRUCTURE": {
            "RAINSTORM": {
                "$VAR1": "null-sem+"
            }
        }
    }
}

#
suffer_v1 = {
    "SUFFER-V1": {
        "DEFINITION": "the construction ‘to suffer a MEDICAL-­E VENT ’",
        "EXAMPLE": "He suffered a heart attack (a seizure, a stroke).",

        "SYNTACTIC-STRUCTURE": {
            "SUBJECT": "$VAR1",
            "V": "$VAR0",
            "DIRECTOBJECT": "$VAR2"
        },

        "SEMANTIC-STRUCTURE": {
            "^$VAR2(sem MEDICAL-EVENT)": {
                "EXPERIENCER": "^$VAR1"
            }
        },

        "SYNONYMS": "HAVE"
    }
}

#
teach_v1 = {
    "TEACH-V1": {
        "DEFINITION": "to teach someone some subject matter",
        "EXAMPLE": "Mary taught John physics.",

        "SYNTACTIC-STRUCTURE": {
            "SUBJECT": "$VAR1",
            "V": "$VAR0",
            "INDIRECTOBJECT": "$VAR3",
            "DIRECTOBJECT": "$VAR2"
        },

        "SEMANTIC-STRUCTURE": {
            "TEACH": {
                "AGENT": "^$VAR1",
                "THEME": "^$VAR2",
                "BENEFICIARY": "^$VAR3"
            }
        }
    }
}


#
turn_v12 = {
    "TURN-V12": {
        "DEFINITION": "The expression ‘Turn right at the light.’",
        "EXAMPLE": "Turn right at the light.",

        "SYNTACTIC-STRUCTURE": {
            "V": "$VAR0(form infinitive)",
            "ADV": "$VAR1(root 'right')",
            "PP": {  # prep? preposition?
                "PREP": "$VAR2(root 'at')",
                "OBJ": "$VAR3(root 'light')"
            }
        },

        "SEMANTIC-STRUCTURE": {}  # missing
    }
}


#
#  Syntactically similar senses:
#  • in-­prep14: DURING (In the interview he said ...)
#  • in-­prep17: TIME (a meeting in January)
in_prep1 = {
    "IN-PREP1": {
        "DEFINITION": "refers to the physical location of an object or event",
        "EXAMPLE": "The cat in the study is sleeping (the pp modifies ‘cat’). The cat is sleeping in the study (the pp modifies ‘sleeping’).",

        "SYNTACTIC-STRUCTURE": {
            "ROOT": "$VAR1(cat(n v))",
            "PP": {
                "PREP": "$VAR0",
                "OBJ": "$VAR2"
            }
        },

        "SEMANTIC-STRUCTURE": {
            "^$VAR1": {
                "LOCATION": "^$VAR2"
            }
        }
    }
}

# UMBRELLA SENSE OF IN
in_prep501 = {
    "IN-PREP501": {
        "DEFINITION": "the umbrella sense for several senses of ‘in’",

        "SYNTACTIC-STRUCTURE": {
            "ROOT": "$VAR1(cat(n v))",
            "PP": {
                "PREP": "$VAR0",
                "OBJ": "$VAR2"
            }
        },

        "SEMANTIC-STRUCTURE": {
            "^$VAR1": {
                "LOCATION": "^$VAR2"
            }
        },

        "MEANING-PROCEDURES": {
            "SEEK-SPECIFICATION": {
                "RELATION": "[in-prep1/14/17]"
            }
        }
    }
}


#
happy_adj1 = {
    "HAPPY-ADJ1": {
        "DEFINITION": "experiencing a positive feeling",
        "EXAMPLE": "a happy chipmunk",

        "SYNTACTIC-STRUCTURE": {
            "ADJ": "$VAR0",
            "N": "$VAR1"
        },

        "SEMANTIC-STRUCTURE": {
            "HAPPINESS": {
                "DOMAIN": "^$VAR1",
                "RANGE": .8
            }
        },
    }
}

#
out_of_prep2 = {
    "DEFINITION": "The construction ‘NUM out of NUM N’",
    "EXAMPLE": "three out of four dentists",

    "SYNTACTIC-STRUCTURE": {
        "NUM": "$VAR1",
        "PREP": "$VAR0",
        "NUM_": "$VAR2",  # THIS CANT BE DICTS
        "N": "$VAR3"
    },

    "SEMANTIC-STRUCTURE": {
        "MEMBER-TYPE": "$VAR3",
        "QUANT": "refsem1"
    },

    "MEANING-PROCEDURES": [
        "refsem1 = (value^$VAR1 / value^$VAR2)"
    ]
}

#
and_conj31 = {
    "DEFINITION": "The construction ‘the ORD and ORD most ADJ N’",
    "EXAMPLE": "the fourth and fifth most impor­tant companies",

    "SYNTACTIC-STRUCTURE": {
        "DET": "$VAR1(root 'the')",
        "NUM": "$VAR2(type ordinal)",
        "AND": "$VAR0",
        "NUM_": "$VAR3(type ordinal)",
        "ADV": "$VAR4(root 'most')",
        "ADJ": "$VAR5",
        "N": "$VAR6"
    },

    "SEMANTIC-STRUCTURE": {
        "SET": {
            "MEMBER-TYPE": "^$VAR6",
            "ELEMENTS": ["REFSEM1", "REFSEM2"]
        },
        "^$VAR1": "null-sem+",
        "^$VAR4": "null-sem+"
    },

    "MEANING-PROCEDURES": [
        "refsem1 = ^$VAR6-#1corporation (^$VAR5importance set-#1.ordinality.^$VAR2fourth)",
        "value refsem2 = ^$VAR6-#2corporation (^$VAR5importance set-#1.ordinality.^$VAR3fourth)"
    ]
}
