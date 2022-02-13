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
    var msg: string = ""
    var pass = true

    for (let n=0; n< received.length; n++) {
        const f = received[n]
        if (!arrayIncludes(expected,f)) {
            msg += `- ${f}\n`
            pass = false
        }
    }

    for (let n=0; n< expected.length; n++) {
        const f = expected[n]
        if (!arrayIncludes(expected,f)) {
            msg += `+ ${f}\n`
            pass = false
        }
    }

    const message = () => {
        return msg
    }

    return {
      message,
      pass,
    };
  },
});
