# pip install Owlready2
# https://owlready2.readthedocs.io
from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

# Functional -> Only one property value
# has_ or has_for ?

# Are concept classes or intances?
# Are instances classes or instances?


# Classes (T-Box)
with onto:
    #
    class LexicalCategory(Thing):
        pass

    v_lc = LexicalCategory("V")
    n_lc = LexicalCategory("N")

    #
    class Validity(Thing):
        pass

    valid = Validity("Valid")
    invalid = Validity("Invalid")

    class Concept(Thing):
        pass

    # class TMRInstance(Thing):
    #     pass

    class has_for_agent(ObjectProperty, FunctionalProperty):
        domain = [Concept]
        range = [Concept]

    class has_for_theme(ObjectProperty, FunctionalProperty):
        domain = [Concept]
        range = [Concept]

    class is_agent_of(ObjectProperty, FunctionalProperty):
        domain = [Concept]
        range = [Concept]
        inverse_property = has_for_agent

    class is_theme_of(ObjectProperty, FunctionalProperty):
        domain = [Concept]
        range = [Concept]
        inverse_property = has_for_theme

    class validity(DataProperty, FunctionalProperty):
        range = [bool]

    class validity(DataProperty, FunctionalProperty):
        range = [bool]

    class validityb(ObjectProperty, FunctionalProperty):
        range = [Validity]

    #
    class LexicalSense(Thing):
        pass

    class has_for_concept(ObjectProperty, FunctionalProperty):
        domain = [LexicalSense]
        range = [Concept]

    class has_for_category(ObjectProperty, FunctionalProperty):
        domain = [LexicalSense]
        range = [LexicalCategory]

    class has_for_time(DataProperty, FunctionalProperty):
        domain = [LexicalSense]
        range = [str]

    class is_concept_of(ObjectProperty):
        domain = [Concept]
        range = [LexicalSense]
        inverse_property = has_for_concept

    #
    class Verb(LexicalSense):
        equivalent_to = [LexicalSense & has_for_category.value(v_lc)]

    class Noun(LexicalSense):
        equivalent_to = [LexicalSense & has_for_category.value(n_lc)]

    rule = Imp()
    # rule.set_as_rule("""Drug(?d), price(?d, ?p), number_of_tablets(?d, ?n), divide(?r, ?p, ?n) -> validity(?d, True)""")

    AllDisjoint([LexicalCategory, LexicalSense, Concept])
    AllDisjoint([Verb, Noun])

    class Animal(Concept):
        pass

    class Food(Concept):
        pass

    class Event(Concept):
        pass

    class Squirrel(Animal):
        pass

    class Ingest(Event):
        # Theme -> Food
        # Agent -> Animal

        # Wrong:
        # validityb = [Ingest & has_for_agent.some(Animal) & has_for_theme.some(Food)]
        # equivalent_to = [Event & has_for_agent.some(Animal) & has_for_theme.some(Food)]

        # def is_valid(self):
        #     # Problem, no readoner involved
        #     print(self.has_for_theme.is_instance_of)
        #     return True
        pass

    # rule.set_as_rule("Ingest(?i), has_for_theme(?i, ?t), Food(?t), has_for_agent(?i, ?a), Animal(?a) -> validity(?i, true)")

    class IngestValidated(Ingest):
        equivalent_to = [Ingest & has_for_agent.some(Animal) & has_for_theme.some(Food)]

    class Nut(Food):
        pass

    AllDisjoint([Animal, Food, Event])


with onto:
    # Instances (A-Box)
    squirrel_i = Squirrel("Squirrel_c")
    ingest_i = Ingest("Ingest_c")
    nut_i = Nut("Nut_c")

    ingest_i.has_for_agent = squirrel_i
    ingest_i.has_for_theme = nut_i

    squirrel_w = LexicalSense("Squirrel_w")
    eat_w = LexicalSense("Eat_w")
    nut_w = LexicalSense("Nut_w")

    squirrel_w.has_for_concept = squirrel_i
    squirrel_w.has_for_category = n_lc

    eat_w.has_for_concept = ingest_i
    eat_w.has_for_category = v_lc
    eat_w.has_for_time = "PRESENT"

    nut_w.has_for_concept = nut_i
    nut_w.has_for_category = n_lc


#
with onto:
    sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
    pass

print()

print("has_for_agent.domain", has_for_agent.domain)

print("ingest_i.has_for_agent", ingest_i.has_for_agent)
print("ingest_i.has_for_theme", ingest_i.has_for_theme)
print("ingest_i.validity", ingest_i.validity)
# print("ingest_i.is_valid()", ingest_i.is_valid())
print("nut_i.is_theme_of", nut_i.is_theme_of)
print("nut_i.validity", nut_i.validity)

print()

# c = eat_w's ci
# t = theme of c
# w = word with t as ci
# is w a verb?

r = default_world.sparql("""

   SELECT (COUNT(?x) AS ?nb)
   { ?x a owl:Class . }
""")

print(list(r))

with open('ontology.owl', 'wb') as f:
    onto.save(file=f)


#
