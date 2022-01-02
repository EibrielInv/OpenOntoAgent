# TMRs
# Text Meaning Representation


sentence_3 = {
    "text": "Audrey",

    "HUMAN-1": {
        "GENDER": "female",
        "HAS-PERSONAL-NAME": "Audrey"
    }
}

# candidate 1
sentence_4 = {
    "text": "Audrey killed",

    "KILL-1": {
        "AGENT": "HUMAN1",
        "TIME": "<find-anchor-time"
    },

    "HUMAN-1": {
        "GENDER": "female",
        "HAS-PERSONAL-NAME": "Audrey"
    }
}

# candidate 2
sentence_5 = {
    "text": "Audrey killed",

    "VETO-1": {
        "AGENT": "HUMAN1",
        "TIME": "<find-anchor-time"
    },

    "HUMAN-1": {
        "GENDER": "female",
        "HAS-PERSONAL-NAME": "Audrey"
    }
}

# candidate 3
sentence_6 = {
    "text": "Audrey killed",

    "ASPECT-1": {
        "PHASE": "end",
        "SCOPE": "OPERATE-DEVICE-1"
    },

    "OPERATE-DEVICE-1": {
        "AGENT": "HUMAN-1",
        "TIME": "<find-anchor-time"
    },

    "HUMAN-1": {
        "GENDER": "female",
        "HAS-PERSONAL-NAME": "Audrey"
    }
}

# candidate 3
sentence_7 = {
    "text": "Audrey killed the motor",

    "ASPECT-1": {
        "PHASE": "end",
        "SCOPE": "OPERATE-DEVICE-1"
    },

    "OPERATE-DEVICE-1": {
        "AGENT": "HUMAN-1",
        "THEME": "MOTOR-1",
        "TIME": "<find-anchor-time"
    },

    "HUMAN-1": {
        "GENDER": "female",
        "HAS-PERSONAL-NAME": "Audrey"
    }
}

#

sentence_2 = {
    "text": "A gray squirrel ate a nut.",

    "INGEST-1": {
        "AGENT": "SQUIRREL-1",
        "THEME": "NUT-FOODSTUFF-1",
        "TIME": "< FIND-ANCHORT-TIME",
        "from-sense": "EAT-V1",
        "word-num": 3
    },

    "SQUIRREL-1": {
        "COLOR": "gray",
        "AGENT-OF": "INGEST-1",
        "from-sense": "SQUIRREL-N1",
        "word-num": 2
    },

    "NUT-FOODSTUFF-1": {
        "THEME-OF": "INGEST-1",
        "from-sense": "NUT-N1",
        "word-num": 5
    }
}


"""
The newly acquired meaning repre­sen­ta­tion is related to a stored memory via ontological
paraphrase. Ontological paraphrase occurs when more than one metalanguage repre­sen­
ta­tion means the same ­thing.
"""


tmr_1 = {
    "text": "go to London by plane",

    "MOTION-EVENT-7": {
        "DESTINATION": "CITY-50",
        "INSTRUMENT": "AIRPLANE-1"
    },

    "CITY-50": {
        "HAS-NAME": "London"
    }
}

tmr_2 = {
    "text": "fly to London",

    "AERIAL-MOTION-EVENT-19": {
        "DESTINATION": "CITY-50"
    },

    "CITY-50": {
        "HAS-NAME": "London"
    }
}


#
question_1 = {
    "text": "Do you have any discomfort in your esophagus?",

    "REQUEST-INFO-1": {
        "AGENT": "HUMAN-2",  # THE PHYSICIAN
        "THEME": "MODALITY-1",  # THE VIRTUAL PATIENT
        "BENEFICIARY": "HUMAN-1",
        "MODALITY-1": {
            "TYPE": "EPISTEMIC",
            "SCOPE": "DISCOMFORT-1"
        },
        "DISCOMFORT-1": {
            "EXPERIENCER": "HUMAN-1",  # THE VIRTUAL PATIENT
            "LOCATION": "ESOPHAGUS-1"
        },
        "ESOPHAGUS-1": {
            "PART-OF-OBJECT": "HUMAN-1"  # THE VIRTUAL PATIENT
        }
    }
}

#
discomfort_1 = {
    "text": "Discomfort in your esophagus",

    "DISCOMFORT-1": {
        "EXPERIENCER": "HUMAN-1",
        "LOCATION": "ESOPHAGUS-1"
    },
    "ESOPHAGUS-1": {
        "PART-OF-OBJECT": "HUMAN-1"
    }
}

#
symptom_1 = {
    "text": "Symptom in its chest",

    "SYMPTOM-1": {
        "EXPERIENCER": "HUMAN-1",
        "LOCATION": "CHEST-1"
    },
    "CHEST-1": {
        "PART-OF-OBJECT": "HUMAN-1"
    }
}

#
"""
To give just one example of how much easier it is for p ­ eople to read bunched outputs,
consider the TMR for the sentence A pirate was attacked by a security guard in which the
available analyses of pirate and attack are bunched (and security guard is unambiguous).
"""
pirate_1 = {
    "text": "A pirate was attacked by a security guard",

    "PHYSICAL-­EVENT-1": {
        "AGENT": "SECURITY-GUARD-1",
        "THEME": "HUMAN-1",
        "TIME": "<find-anchor-time",
        "BUNCHED-FROM": [
            "ATTACK(attack-v1)",
            "CRITICIZE(attack-v2)"
        ]
    },

    "HUMAN-1": {
        "BUNCHED-FROM": [
            "PIRATE-AT-SEA(pirate-n1)",
            "INTELLECTUAL-PROPOERTY-THIEF(pirate-n2)"
        ]
    }
}


#
sailor_1 = {
    "text": "A sailor threw some food overboard",


    "THROW-1": {
        "AGENT": "SAILOR-1",
        "THEME": "FOOD-1",
        "SOURCE": "SURFACE-WATER-VEHICLE",
        "DESTINATION": "BODY-OF-WATER",
        "TIME": "<find-anchor-time"
    }
}

sailor_2 = {
    "text": "A sailor threw some food overboard into the Mediterranean Sea",


    "THROW-1": {
        "AGENT": "SAILOR-2",
        "THEME": "FOOD-2",
        "SOURCE": "SURFACE-WATER-VEHICLE",
        "DESTINATION": "SEA-5",
        "TIME": "<find-anchor-time"
    },

    "SEA-5": {
        "HAS-NAME": "Mediterranean Sea",
        "DESTINATION-OF": "THROW-2"
    }
}

"""
Respectively

Sets:
SET
MEMBER-­TYPE; an ontological concept
ELE­MENTS; a list of concept instances
NOT-­ELEMENTS; a list of concept instances or a pointer to another set
QUANT; 0–1, indicating a relative amount or percentage
CARDINALITY; any integer
RELATIVE-­TO-­NORM; 0–1 (used to describe words like ‘too’ in ‘too many’)
HAS-­SUBSET; a pointer to another set
SUBSET-­OF; a pointer to another set
COMPLETE; yes or no
ORDINALITY; any integer
SET-­T YPE; conjunctive or disjunctive
any property; any valid filler for the given property
"""

order_1 = {
    "text": "The doctor and the nurse ordered soup and spaghetti.",

    "ORDER-IN-RESTAURANT-1": {
        "AGENT": "SET-1",
        "THEME": "SET-2"
    },

    "SET-1": {
        "ELEMENTS": ["PHYSICIAN-1", "NURSE-1"],
        "CARDINALITY": 2
    },

    "SET-2": {
        "ELEMENTS": ["SOUP-1", "SPAGHETTI-MEAL-1"],
        "CARDINALITY": 2
    }
}

order_2 = {
    "text": "The doctor and the nurse ordered soup and spaghetti, respectively.",

    "ORDER-IN-RESTAURANT-1": {
        "AGENT": "PHYSICIAN-1",
        "THEME": "SOUP-1"
    },

    "ORDER-IN-RESTAURANT-2": {
        "AGENT": "NURSE-1",
        "THEME": "SPAGHETTI-MEAL-1"
    }
}

wolves = {
    "text": "wolves",

    "SET-1": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": ">1"
    }
}

many_wolves = {
    "text": "too many gray wolves",

    "SET-2": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": ">1",
        "RELATIVE-TO-NORM": ">0.6",
        "COLOR": "gray"
    }
}

two_gray_wolves = {
    "text": "two gray wolves",

    "SET-3": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": "2",
        "COLOR": "gray"
    }
}

both_wolves = {
    "text": "both wolves",

    "SET-4": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": "2",
        "COMPLETE": "yes"
    }
}

persent_wolves = {
    "text": "80% of wolves",

    "SET-5": {
        "MEMBER-TYPE": "WOLF",
        "QUANT": ".8"
    }
}

a_lot_of_wolves = {
    "text": "a lot of wolves",

    "SET-6": {
        "MEMBER-TYPE": "WOLF",
        "QUANT": ".7<>.9"
    }
}

two_hungry_wolves = {
    "text": "two of the wolves are hungry",

    "SET-7": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": ">2",
        "HAS-SUBSET": "SET-8"
    },

    "SET-8": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": "2",
        "EXPERIENCER-OF": "HUNGER-1",
        "SUBSET-OF": "SET-7"
    }
}

except_whiskers = {
    "text": "all of the wolves except for Whiskers",

    "SET-9": {
        "MEMBER-TYPE": "WOLF",
        "QUANT": 1,
        "NOT-ELEMENTS": "WOLF-1"
    },

    "WOLF-1": {
        "HAS-PERSONAL-NAME": "Whiskers"
    }
}

gray_wolves_are_sleeping = {
    "text": "Gray wolves are sleeping",

    "SET-10": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": ">1",
        "COLOR": "gray",
        "EXPERIENCER-OF": "SLEEP-1"
    }
}

# First stage
both_gray_wolves_are_sleeping_1 = {
    "text": "both gray wolves are sleeping",

    "SET-1": {
        "MEMBER-TYPE": "WOLF",
        "CARDINALITY": "2",
        "COMPLETE": "yes",
        "COLOR": "gray",
        "EXPERIENCER-OF": "SLEEP-1"
    }
}

# second stage
both_gray_wolves_are_sleeping_2 = {
    "text": "both gray wolves are sleeping",

    "SET-1": {
        "ELEMENTS": ["WOLF-1", "WOLF-2"],
        "CARDINALITY": "2",
        "COMPLETE": "yes"
    },

    "SLEEP-1": {
        "EXPERIENCER": "WOLF-1"
    },

    "WOLF-1": {
        "MEMBER-OF": "SET-1",
        "COLOR": "gray",
        "EXPERIENCER-OF": "SLEEP-1"
    },

    "SLEEP-2": {
        "EXPERIENCER": "WOLF-2"
    },

    "WOLF-2": {
        "MEMBER-OF": "SET-1",
        "COLOR": "gray",
        "EXPERIENCER-OF": "SLEEP-2"
    }
}

#
out_of_1 = {
    "text": "Nine out of ten people",

    "SET-1": {
        "MEMBER-TYPE": "HUMAN",
        "QUANT": .9
    }
}


out_of_2_1 = {
    "text": "the fourth and fifth most impor­tant companies",

    "SET": {
        "MEMBER-TYPE": "CORPORATION",
        "ELEMENTS": ["refsem1", "refsem2"]
    },

    "refsem1": {
        "CORPORATION-1": {
            "IMPORTANCE": "SET-1.ORDINALITY.4"
        }
    },

    "refsem2": {
        "CORPORATION-2": {
            "IMPORTANCE": "SET-1.ORDINALITY.5"
        }
    }
}


out_of_2_2 = {
    "text": "the fourth and fifth most impor­tant companies",

    "SET": {
        "MEMBER-TYPE": "CORPORATION",
        "ELEMENTS": ["CORPORATION-1", "CORPORATION-2"]
    },

    "CORPORATION-1": {
        "IMPORTANCE": "SET-1.ORDINALITY.4"
    },

    "CORPORATION-2": {
        "IMPORTANCE": "SET-1.ORDINALITY.5"
    }
}


and_2 = {
    "text": "the second and third most popu­lar TV shows",

    "SET-1": {
        "MEMBER-TYPE": "TELEVISION-PROGRAM",
        "ELEMENTS": ["TELEVISION-PROGRAM-1", "TELEVISION-PROGRAM-2"]
    },

    "TELEVISION-PROGRAM-1": {
        "POPULARITY": "SET-1.ORDINALITY.2"
    },

    "TELEVISION-PROGRAM-2": {
        "POPULARITY": "SET-1.ORDINALITY.3"
    }
}


#

sample_1 = {
    "text": "Shehan told him about the layoffs.",

    "DISMISS-1": {
        "THEME-OF": "INFORM-1",
        "THEME-OF-1": "DESCRIBE-1",
        "CARDINALITY": [">", 1],
        "token": "layoffs",
        "from-sense": "LAYOFF-N1"
    },

    "INFORM-1": {
        "AGENT": "HUMAN-1",
        "THEME": "DISMISS-1",
        "HAS-EVENT-AS-PART": "DESCRIBE-1",
        "BENEFICIARY": "HUMAN-2",
        "TIME": ["<", "FIND-ANCHOR-TIME"],
        "token": "told",
        "from-sense": "TELL-V13"
    },

    "HUMAN-2": {
        "GENDER": "MALE",
        "BENEFICIARY-OF": "INFORM-1",
        "token": "him",
        "from-sense": "HE-N1",
    },

    "DESCRIBE-1": {
        "AGENT": "HUMAN-1",
        "THEME": "DISMISS-1",
        "PART-OF-EVENT": "INFORM-1",
        "token": "told",
        "from-sense": "TELL-V13"
    },

    "HUMAN-1": {
        "HAS-PERSONAL-NAME": "SHEHAN",
        "AGENT-OF": "INFORM-1",
        "AGENT-OF-1": "DESCRIBE-1",
        "token": "Shehan",
        "from-sense": "PERSON-NAME"
    }
}
