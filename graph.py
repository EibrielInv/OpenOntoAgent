# Constraint

#  A Brown Squirrel Is Eating a Nut

"""

Ingest#1
- Agent: Squirrel#1
- Theme: Nut#1
- Time: Now

Squirrel#1
- Color: Brown
- Concept: Squirrel
- Agent-of: Ingest#1

Nut#1
- Theme-of: Ingest#1
- Concept: Nut


-------------------------------

Ingest#1
- Agent: Squirrel#1
            - Color: Brown
            - Concept: Squirrel
                - Is-a: Animal
            - Agent-of: Ingest#1
- Theme: Nut#1
            - Theme-of: Ingest#1
            - Concept: Nut
                - Is-a: Food
- Time: Now


-------------------------------


"Eat"
- Ingest
- V

"Nut"
- Nut
- N

"Squirrel"
- Squirrel
- N

------------------------------


"Eat"
- Subject (N):
    - "Squirrel"
- Object (N):
    - "Nut"


-----------------------------

"""
