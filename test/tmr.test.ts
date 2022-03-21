import {Ontoagent} from "../src/index"

import fs from 'fs'
import YAML from 'yaml'


const file = fs.readFileSync('src/resources/knowledge.yaml', 'utf8')
console.log(YAML.parse(file))

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
        [2,"tmr.instance.property/property",3],
        [3,"tmr.instance.property/name","AGENT"],
        [3,"tmr.instance.property/value","SQUIRREL-1"],

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
        [2,"tmr.instance.property/property",3],
        [3,"tmr.instance.property/name","CONCEPT"],
        [3,"tmr.instance.property/value","INGEST"],

    ]

    expect(o.datascript.query()).toBeSameDB(result)
})
