// https://leetcode.com/problems/longest-substring-without-repeating-characters/

/* 
  Given a string, find the length of the longest substring without repeating characters.
*/

const str1 = "abcabcbb";
const expected1 = 3;
// Explanation: The answer is "abc", with the length of 3.

const str2 = "bbbbb";
const expected2 = 1;
// Explanation: The answer is "b", with the length of 1.

const str3 = "pwwkew";
const expected3 = 3;
/* Explanation: The answer is "wke", with the length of 3. 
  Note that the answer must be a substring, "pwke" is a subsequence and not a substring. */

const str4 = "dvadf";
const expected4 = 4;
// Explanation: "vadf"

/**
 * Determines the length of the longest substring in the given str.
 * @param {string} str
 * @returns {number} Length of the longest substring from the given str.
 * - Time: O(?).
 * - Space: O(?).
 */
function lengthOfLongestSubString(str) { }

// =======================================================================================================


/* 
    Bogo Sort works by shuffling the elements then checking if the array is sorted. If the array is not sorted then you shuffle and check again until it is sorted.
*/

const testArr1 = [8, 4, 2];

const testArr2 = [8, 4, 2, 9]

const testArr3 = [8, 4, 2, 9, 5, 12] // might take a while for this one unless you get lucky.

function bogoSort(str) { }


function lengthOfLongestSubString(str) {
    let newObj = {};
    let maxCount = 0;
    let counter = 0;
    for (let i = 0; i < str.length; i++) {
        for (let j = i; j < str.length; j++) {
            if (!newObj[str[j]]) {
                newObj[str[j]] = 1
                counter++
            } else {
                if (counter > maxCount) {
                    maxCount = counter
                }
                newObj = {};
                counter = 0;
            }
        }
    }
    return maxCount;
}