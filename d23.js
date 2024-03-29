/* 
  November 10, 2022
Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */

/*****************************************************************************/
function fewestCoinChange(cents) {

    var dict = {'pennies': 0, 'nickels': 0, 'dimes': 0, 'quarters': 0, 'halfDollars': 0};

    // while(cents >= 50){
    //     dict['halfDollars']++;
    //     cents -= 50
    // }
    while(cents >= 25){
        dict['quarters']++;
        cents -= 25
    }
    while(cents >= 10){
        dict['dimes']++;
        cents -= 10
    }
    while(cents >= 5){
        dict['nickels']++;
        cents -= 5
    }
    while(cents >= 1){
        dict['pennies']++;
        cents -= 1
    }
    return dict;
}