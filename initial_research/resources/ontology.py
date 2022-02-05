# Ontological description

ingest = {
    "INGEST": {
        "AGENT": {
            "SEM": "ANIMAL",
            "RELAXABLE-TO": "SOCIAL-OBJECT"
        },
        "THEME": {
            "SEM": "FOOD,BEVERAGE,INDESTIBLE-MEDICATION",
            "RELAXABLE-TO": "ANIMAL,PLANT",
            "NOT": "HUMAN"
        }
    }
}


drug_dealing = {
    "DRUG-DEALING": {
        "IS-A": {
            "VALUE": "CRIMINAL-ACTIVITY"
        },
        "AGENT": {
            "DEFAULT": "CRIMINAL,DRUG-CARTEL",
            "SEM": "HUMAN",
            "RELAXABLE-TO": "SOCIAL-OBJECT"
        },
        "THEME": {
            "DEFAULT": "ILLEGAL-DRUG"
        },
        "INSTRUMENT": {
            "SEM": "MONEY"
        },
        "HAS-EVENT-AS-PART": {
            "SEM": "BUY,SELL"
        },
        "LOCATION": {
            "DEFAULT": "CITY",
            "SEM": "PLACE",
            "RELAXABLE-TO": "PHYSICAL-OBJECT"
        }
    }
}


# Incomplete
poodle = {
    "POODLE": {
        "COLOR": {
            "DEFAULT": "black,white,brown,tan",
            "SEM": "silver,orange"
        },
        "INTELLIGENCE": {
            "DEFAULT": .9
        },
        "FRIENDLINESS": {
            "DEFAULT": .9
        },
        "FUR-TYPE": {
            "VALUE": "curly-hair"
        },
        "EASE-OF-TRAINING": {
            "DEFAULT": .9
        }
    }
}


#
aerial_mition_event = {
    "AERIAL-MOTION-EVENT": {
        "IS-A": {
            "VALUE": "MOTION-EVENT"
        },
        "INSTRUMENT": {
            "DEFAULT": "AIRPLANE",
            "SEM": "HELICOPTER, BALLOON-TRANSPORTATION"
        }
    }
}


#
happiness = {
    "HAPPINESS": {
        "DOMAIN": "ANIMAL",
        "RANGE": [0, 1]
    }
}

marital_status = {
    "MARITAL-STATUS": {
        "DOMAIN": "HUMAN",
        "RANGE": ["single", "married", "divorced", "widowed"]
    }
}

experiencer_of = {
    "EXPERIENCER-OF": {
        "DOMAIN": "ANIMAL",
        "RANGE": "EVENT"
    }
}
