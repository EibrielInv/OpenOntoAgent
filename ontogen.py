from resources.complete.squirrel import tmr, lexicon, ontology


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
for l in tmr["TMR"]:
    concept = tmr["TMR"][l]["CONCEPT"]
    # print()
    # print(concept)
    lexical_sense = find_lexical_sense(concept)
    lexical_senses.append(lexical_sense)
    # print(lexical_sense[1].lower())
    # print(lexical_sense[0])

for ls in lexical_senses:
    # print(ls)
    lexical_sense = ls[0]
    if type(lexical_sense["SEM-STRUC"]) == dict:
        for c in lexical_sense["SEM-STRUC"]:
            for p in lexical_sense["SEM-STRUC"][c]:
                print(lexical_sense["SEM-STRUC"][c][p]["VALUE"])
                print(ontology[c][p]["SEM"])
