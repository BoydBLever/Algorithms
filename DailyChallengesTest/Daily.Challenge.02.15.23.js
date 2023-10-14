// https://leetcode.com/problems/add-to-array-form-of-integer/submissions/898639965/
/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let carry = 0;
    let i = num.length - 1;
    let result = [];

    while (i >= 0 || k > 0 || carry > 0) {
        let sum = (i >= 0 ? num[i] : 0) + (k % 10) + carry;
        result.unshift(sum % 10);
        carry = Math.floor(sum / 10);
        i--;
        k = Math.floor(k / 10);
    }

    return result;
};
