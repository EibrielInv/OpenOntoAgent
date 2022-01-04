import pprint
import copy
from resources.complete.squirrel import tmr, lexicon, ontology

from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.microplanning import *

pp = pprint.PrettyPrinter(indent=4)


def find_lexical_sense(concept):
    for l in lexicon:
        for ll in lexicon[l]:
            sem_struc = lexicon[l][ll]["SEM-STRUC"]
            if type(sem_struc) == str:
                if sem_struc == concept:
                    return [lexicon[l][ll], l]
            elif type(sem_struc) == dict:
                if concept in sem_struc:
                    return [lexicon[l][ll], l]


lexical_senses = []
tmr_extended = copy.deepcopy(tmr)
for l in tmr["TMR"]:
    concept = tmr["TMR"][l]["CONCEPT"]
    # print()
    # print(concept)
    lexical_sense = find_lexical_sense(concept)
    lexical_senses.append(lexical_sense)
    # print(lexical_sense[1].lower())
    # print(lexical_sense[0])
    tmr_extended["TMR"][l]["lexical_sense"] = copy.deepcopy(lexical_sense[0])
    tmr_extended["TMR"][l]["word"] = copy.deepcopy(lexical_sense[1])

print()
print("TMR")
pp.pprint(tmr_extended)

root = None
# Find root
for l in tmr_extended["TMR"]:
    sem_struc = tmr_extended["TMR"][l]["lexical_sense"]["SEM-STRUC"]
    # If complex sem struc
    if type(sem_struc) == dict:
        root = l

# Fill AGENT

print("Root:")
pp.pprint(root)

tmr_extended["TMR"][root]["lexical_sense_filled"] = copy.deepcopy(tmr_extended["TMR"][root]["lexical_sense"])

tmr_extended["TMR"][root]["lexical_sense_filled"]["SEM-STRUC"]["INGEST"]["AGENT"]["VALUE"] = tmr_extended["TMR"][root]["AGENT"]
tmr_extended["TMR"][root]["lexical_sense_filled"]["SEM-STRUC"]["INGEST"]["THEME"]["VALUE"] = tmr_extended["TMR"][root]["THEME"]

# tmr_extended["TMR"][root]["lexical_sense_filled"] = tmr_extended["TMR"][root]["lexical_sense"]
tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["DIRECTOBJECT"]["ROOT"] = tmr_extended["TMR"][root]["THEME"]
tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["ROOT"] = root
tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["SUBJECT"]["ROOT"] = tmr_extended["TMR"][root]["AGENT"]

print("TMR B")
pp.pprint(tmr_extended)

print("Syntactic Structure")
pp.pprint(tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"])

words = []

words.append({
    "id": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["ROOT"],
    "cat": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["CAT"],
    "word": tmr_extended["TMR"][tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["ROOT"]]["word"],
    "root": True,

    "directobject_id": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["DIRECTOBJECT"]["ROOT"],
    "subject_id": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["SUBJECT"]["ROOT"],

    "directobject_word": tmr_extended["TMR"][tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["DIRECTOBJECT"]["ROOT"]]["word"],
    "subject_word": tmr_extended["TMR"][tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["SUBJECT"]["ROOT"]]["word"]
})

words.append({
    "id": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["DIRECTOBJECT"]["ROOT"],
    "cat": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["DIRECTOBJECT"]["CAT"],
    "word": tmr_extended["TMR"][tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["DIRECTOBJECT"]["ROOT"]]["word"]
})

words.append({
    "id": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["SUBJECT"]["ROOT"],
    "cat": tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["SUBJECT"]["CAT"],
    "word": tmr_extended["TMR"][tmr_extended["TMR"][root]["lexical_sense_filled"]["SYN-STRUC"]["SUBJECT"]["ROOT"]]["word"]
})

print("Words")
pp.pprint(words)

realise_en = Realiser(host='nlg.kutlak.info', port=40000)

p = Clause()
for w in words:
    if "root" in w and w["root"]:
        p.predicate = VP(w["word"].lower())
        p.subject = NP(w["subject_word"].lower())
        p.object = NP(w["directobject_word"].lower())

# expected = This example shows how cool simplenlg is.
print()
print(realise_en(p))
