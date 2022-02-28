import {Loop} from "../src/index"

const tmr:any = [
    ["INGEST-1",
        [
            ["AGENT", "SQUIRREL-1"],
            ["THEME", "NUT-FOODSTUFF-1"],
            ['TIME', 'FIND-ANCHOR-TIME'],
        ]
    ],

    ["SQUIRREL-1",
        [
            ["COLOR", "BROWN"],
            ["AGENT-OF", "INGEST-1"],
            ["CONCEPT", "SQUIRREL"]
        ]
    ],

    ["NUT-FOODSTUFF-1", [
            ["THEME-OF", "INGEST-1"],
            ["CONCEPT", "NUT-FOODSTUFF"]
        ]
    ]
]

test("Adding empty concept", () => {
    const l = new Loop()

    expect(l.match(tmr)).toBeTruthy()
})
