/**
 * Creates a hash table of case-insensitive categories mapped to the items
 * belonging to that category.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<Object>} items
 * @param {string} items.category
 * @returns {Object<string, Array<Object>>} The hash category hash table with
 *    string keys and array of objects as values.
 */
function groupObjects(items) {
    let outObj = {};

    for (i = 0; i < items.length; i++) {
        console.log(items[i].category.toLowerCase());
        if (!outObj[items[i].category.toLowerCase()]) {
            outObj[items[i].category.toLowerCase()] = [];
            outObj[items[i].category.toLowerCase()].push(items[i]);
        }

        else{
            outObj[items[i].category.toLowerCase()].push(items[i]);
        }
    }

    return outObj;
}

console.log(groupObjects(objects));
/**
 * Determines if the given strings are equal after the backspace characters
 * "#" are processed.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} S
 * @param {string} T
 * @returns {boolean} Whether the given strings are equal after backspaces
 *    have been processed.
 */
function backspaceStringCompare(S, T) {
    let sOut = [];
    let tOut = [];
    let count = 0;

    while (count < S.length || count < T.length) {
        if (count < S.length) {
            if (S[count] === '#') {
                sOut.pop();
            }
            else {
                sOut.push(S[count]);
            }
        }
        if (count < T.length) {
            if (T[count] === '#') {
                tOut.pop();
            }
            else {
                tOut.push(T[count]);
            }
        }
        count++;
    }
    console.log(sOut);
    console.log(tOut);

    if (sOut.toString() == tOut.toString()) {
        return true;
    }

    return false;
}

// console.log(backspaceStringCompare(S1, T1));
// console.log(backspaceStringCompare(S2, T2));
// console.log(backspaceStringCompare(S3, T3));
// console.log(backspaceStringCompare(S4, T4));