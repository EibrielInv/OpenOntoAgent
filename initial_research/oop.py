from constraint import *


# Ontology
class Onto:
    def __init__(self):
        self.ontology = {
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

            "BEVERAGE": {
                "IS-A": "LIQUID"
            },

            "SQUIRREL": {
                "IS-A": "ANIMAL"
            },

            "ANIMAL": {
                "IS-A": "ORGANISM"
            }
        }

    def add_element(self, element, parent):
        pass

    def is_in_group(self, element, group):
        if element == group:
            return True

        if element not in self.ontology:
            return False

        if group == self.ontology[element]["IS-A"]:
            return True

        return False

    def is_match(self, element, position, find):
        data = self.ontology[element][position]["SEM"]
        if type(data) == str:
            return self.is_in_group(find, data)
        elif type(data) == list:
            for l in data:
                if self.is_in_group(find, l):
                    return True
        return False


# Lexicon
lexicon = {
    "SQUIRREL": {
        "CONCEPT": "SQUIRREL",
        "CATEGORY": "NOUN"
    },
    "EAT": {
        "CONCEPT": "INGEST",
        "AGENT": {
            "CATEGORY": "NOUN"
        },
        "THEME": {
            "CATEGORY": "NOUN"
        },
        "CATEGORY": "VERB"
    },
    "DRINK": {
        "CONCEPT": "INGEST",
        "AGENT": {
            "CATEGORY": "NOUN"
        },
        "THEME": {
            "CATEGORY": "NOUN",
            "SEM": "BEVERAGE"
        },
        "CATEGORY": "VERB"
    },
    "NUT": {
        "CONCEPT": "NUT-FOODSTUFF",
        "CATEGORY": "NOUN"
    }
}


def find_worlds_by_concept(concept):
    words = []
    for lex_key in lexicon:
        if lexicon[lex_key]["CONCEPT"] == concept:
            words.append(lex_key)
    return words


# TMR
tmr = {
    "INGEST-1": {
        "AGENT": "SQUIRREL-1",
        "THEME": "NUT-FOODSTUFF-1",
        'TIME': "PAST",
        "CONCEPT": "INGEST"
    },

    "SQUIRREL-1": {
        "COLOR": "BROWN",
        "AGENT-OF": "INGEST-1",
        "CONCEPT": "SQUIRREL"
    },

    "NUT-FOODSTUFF-1": {
        "THEME-OF": "INGEST-1",
        "CONCEPT": "NUT-FOODSTUFF"
    }
}

onto = Onto()

# print(onto.is_in_group("NUT-FOODSTUFF", "FOOD"))

tmrel2words = {}
indexes = []
# For each TMR element find all words
for tmr_element in tmr:
    concept = tmr[tmr_element]["CONCEPT"]
    tmrel2words[tmr_element] = find_worlds_by_concept(concept)
    indexes.append(tmr_element)

# print(tmrel2words)

problem = Problem()

for tmri in indexes:
    problem.addVariable(tmri, tmrel2words[tmri])


def check(*args):
    mapping = {}
    n = 0
    for tmri in indexes:
        mapping[tmri] = args[n]
        n += 1

    mismatch = False
    for tmri in mapping:
        for slot in ["AGENT", "THEME"]:
            if slot in lexicon[mapping[tmri]]:
                # Get current agent concept
                current_element = tmr[tmri][slot]
                current_concept = tmr[current_element]["CONCEPT"]
                element = lexicon[mapping[tmri]]["CONCEPT"]
                if slot in lexicon[mapping[tmri]]:
                    if "SEM" in lexicon[mapping[tmri]][slot]:
                        new_element = lexicon[mapping[tmri]][slot]["SEM"]
                        # print(current_concept, new_element)
                        if not onto.is_in_group(current_concept, new_element):
                            mismatch = True
                if not onto.is_match(element, slot, current_concept):
                    mismatch = True

    return not mismatch


problem.addConstraint(check)

print()

print(problem.getSolutions())


# print(candidates)
