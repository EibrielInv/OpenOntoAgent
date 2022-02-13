export {};

declare global {
  namespace jest {
    interface Matchers<R> {
      toBeSameDB(expected: Array<any>): CustomMatcherResult;
    }
  }
}

function arrayIncludes(array: Array<any>, includes: Array<any>) {
    let match = false
    for (let a=0; a< array.length; a++) {
        if (array[a][0] === includes[0] && array[a][1] === includes[1] && array[a][2] === includes[2]) {
            match = true
        }
    }
    return match
}

expect.extend({
  toBeSameDB(received: Array<any>, expected: Array<any>): jest.CustomMatcherResult {
    var msg_received: string = ""
    var msg_expected: string = ""
    var pass = true

    for (let n=0; n< received.length; n++) {
        const f = received[n]
        if (!arrayIncludes(expected,f)) {
            msg_received += JSON.stringify(f)+",\n"
            pass = false
        }
    }
    if (msg_received != "") {
        msg_received = "Missing:\n"+msg_received
    }

    for (let n=0; n< expected.length; n++) {
        const f = expected[n]
        if (!arrayIncludes(received,f)) {
            msg_expected += JSON.stringify(f)+",\n"
            pass = false
        }
    }
    if (msg_expected != "") {
        msg_expected = "Extra:\n"+msg_expected
    }

    const message = () => {
        return msg_received + msg_expected
    }

    return {
      message,
      pass,
    };
  },
});
