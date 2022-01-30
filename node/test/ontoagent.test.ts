import {Ontoagent} from "../src/index"

test("Dummy unit test", () => {
    const o = new Ontoagent();

    //expect(o.query()).toBe([[1, "concept/name", "animal"]]);
    expect(o.query()).toStrictEqual([[1, "concept/name", "animal"]]);
});
