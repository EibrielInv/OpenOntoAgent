import {Ontoagent} from "../src/index"

const concepts = {
    "EMPTY-CONCEPT": {},
    "SQUIRREL": {
        "IS-A": "ANIMAL"
    },
    "INGEST": {
        "AGENT": {
            "SEM": "ANIMAL"
        }
    }
}

test("Adding empty concept", () => {
    const o = new Ontoagent()

    o.addConcept("EMPTY-CONCEPT", {})

    const result = [
        [1, "concept/name", "EMPTY-CONCEPT"]
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Concept exists", () => {
    const o = new Ontoagent()

    expect(o.conceptExists("SQUIRREL")).toBeFalsy()

    o.addConcept("SQUIRREL", {})

    expect(o.conceptExists("SQUIRREL")).toBeTruthy()
})

test("Adding concept is-a", () => {
    const o = new Ontoagent()

    o.addConcept("SQUIRREL", concepts["SQUIRREL"])

    const result = [
        [1, "concept/is-a", 2],
        [1, "concept/name", "SQUIRREL"],
        [2, "concept/name", "ANIMAL"],
    ]

    expect(o.query()).toStrictEqual(result)
})

test("Adding concept with property", () => {
    const o = new Ontoagent()

    o.addConcept("INGEST", concepts["INGEST"])

    const result = [
        [1, "concept/is-a", 2],
        [1, "concept/name", "SQUIRREL"],
        [2, "concept/name", "ANIMAL"],
    ]

    expect(o.query()).toStrictEqual(result)
})
