import {Ontoagent} from "../src/index"

const tmr = {
    "TMR": {
        "INGEST-1": {},
        "SQUIRREL-1": {}
    },
    "TMR2": {
        "INGEST-1": {
            "AGENT": "SQUIRREL-1",
        }
    },
    "TMR3": {
        "INGEST-1": {
            "CONCEPT": "INGEST",
        }
    }
}

test("Adding empty tmr", () => {
    const o = new Ontoagent()

    o.tmr.addTmr({})

    const result = [
        [1, "tmr/id", 1]
    ]

    expect(o.datascript.query()).toBeSameDB(result)
})

test("Adding empty instances", () => {
    const o = new Ontoagent()

    o.tmr.addTmr(tmr["TMR"])

    const result = [
        [1, "tmr/id", 1],
        [1,"tmr/instance",2],
        [1,"tmr/instance",3],
        [2,"tmr.instance/id","INGEST-1"],
        [3,"tmr.instance/id","SQUIRREL-1"]
    ]

    expect(o.datascript.query()).toBeSameDB(result)
})

test("Adding instances with instance property", () => {
    const o = new Ontoagent()

    o.tmr.addTmr(tmr["TMR2"])

    const result = [
        [1,"tmr/id", 1],
        [1,"tmr/instance",2],
        [2,"tmr.instance/id","INGEST-1"],
        [2,"semantic-structure.concept.property/property",3],
        [3,"semantic-structure.concept.property/name","AGENT"],
        [3,"semantic-structure.concept.property/value","SQUIRREL-1"],

    ]

    expect(o.datascript.query()).toBeSameDB(result)
})

test("Adding instances with concept property", () => {
    const o = new Ontoagent()

    o.tmr.addTmr(tmr["TMR3"])

    const result = [
        [1, "tmr/id", 1],
        [1,"tmr/instance",2],
        [2,"tmr.instance/id","INGEST-1"],
        [2,"semantic-structure.concept.property/property",3],
        [3,"semantic-structure.concept.property/name","CONCEPT"],
        [3,"semantic-structure.concept.property/value","INGEST"],

    ]

    expect(o.datascript.query()).toBeSameDB(result)
})
