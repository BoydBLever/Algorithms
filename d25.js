//Tuesday, November 17 2022
/*
  Sum To One Digit
  Implement a function sumToOne(num)​ that,
  given a number, sums that number’s digits
  repeatedly until the sum is only one digit. Return
  that final one digit result.
  Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

const num4 = 29756
const expected4 = 2



/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
/*****************************************************************************/
function sumToOneDigit(num) {
    console.log(`Beginning of function, num = ${num}`)
    // edge/base case
    if (!num) {
        console.log(`Nan or 0, returning 0`)
        return 0;
    }

    // base case, single digit
    if (num % 10 == num) {
        console.log(`Single digit, returning ${num}`)
        return num;
    }

    // get sum of digits
    console.log(`${num % 10} + sumToOneDigit(${Math.floor(num / 10)})`);
    sum = (num % 10) + sumToOneDigit(Math.floor(num / 10));

    // If sum has more than one digit, repeats logic; if sum is a single digit, it gets sent back by the second conditional
    return sumToOneDigit(sum);
}

console.log(sumToOneDigit('not a num')); // 0
console.log(sumToOneDigit(0)); // 0
console.log(sumToOneDigit(1)); // 1
console.log(sumToOneDigit(6)); // 6
console.log(sumToOneDigit(23)); // 5
console.log(sumToOneDigit(1234)); // 1

// Same function as a single-line function, with test case 1234
// const sumToOneDigitSL = num => !num ? 0 : num % 10 == num ? num : sumToOneDigitSL(num % 10 + sumToOneDigitSL(Math.floor(num / 10)));

// console.log(sumToOneDigitSL(1234)); // 1