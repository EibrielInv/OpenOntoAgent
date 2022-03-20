import {Ontoagent} from "../src/index"

const tmr = {
    "TMR": {
        "INGEST-1": {
            "CONCEPT": "INGEST",
            "AGENT": "SQUIRREL-1",
            "THEME": "NUTFOODSTUFF-1",
        },
        "SQUIRREL-1": {
            "CONCEPT": "INGEST",
            //"COLOR": "BROWN",
        },
        "NUTFOODSTUFF-1": {
            "CONCEPT": "NUTFOODSTUFF",
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
