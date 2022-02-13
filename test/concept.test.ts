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
    },
    "INGEST-2": {
        "THEME": {
            "RELAXABLE-TO": ["ANIMAL", "PLANT"]
        }
    },
    "INGEST-3": {
        "THEME": {
            "NOT": "HUMAN"
        }
    }
}

test("Adding empty concept", () => {
    const o = new Ontoagent()

    o.addConcept("EMPTY-CONCEPT", {})

    const result = [
        [1, "concept/name", "EMPTY-CONCEPT"]
    ]

    expect(o.query()).toBeSameDB(result)
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

    expect(o.query()).toBeSameDB(result)
})

test("Adding concept with SEM property, with linked concept", () => {
    const o = new Ontoagent()

    o.addConcept("ANIMAL", {})
    o.addConcept("INGEST", concepts["INGEST"])

    const result = [
        [1, "concept/name", "ANIMAL"],
        [2, "concept/name", "INGEST"],
        [2, "concept/property", 3],
        [3, "concept.property/name", "AGENT"],
        [3, "concept.property/semantic", 1],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding concept with SEM property, without linked concept", () => {
    const o = new Ontoagent()

    o.addConcept("INGEST", concepts["INGEST"])

    const result = [
        [1, "concept/name", "INGEST"],
        [1, "concept/property", 2],
        [2, "concept.property/name", "AGENT"],
        [2, "concept.property/semantic", 3],
        [3, "concept/name", "ANIMAL"],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding concept with RELAXABLE-TO property, without linked concepts", () => {
    const o = new Ontoagent()

    o.addConcept("INGEST-2", concepts["INGEST-2"])

    const result = [
        [1, "concept/name", "INGEST-2"],
        [1, "concept/property", 2],
        [2, "concept.property/name", "THEME"],
        [2, "concept.property/relaxable-to", 3],
        [2, "concept.property/relaxable-to", 4],
        [3, "concept/name", "ANIMAL"],
        [4, "concept/name", "PLANT"],
    ]

    expect(o.query()).toBeSameDB(result)
})

test("Adding concept with NOT property, without linked concepts", () => {
    const o = new Ontoagent()

    o.addConcept("INGEST-3", concepts["INGEST-3"])

    const result = [
        [1, "concept/name", "INGEST-3"],
        [1, "concept/property", 2],
        [2, "concept.property/name", "THEME"],
        [2, "concept.property/not", 3],
        [3, "concept/name", "HUMAN"]
    ]

    expect(o.query()).toBeSameDB(result)
})
