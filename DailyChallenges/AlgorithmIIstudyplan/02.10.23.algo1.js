https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=algorithm-ii

// Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "cbaebabacd", p = "abc"
// Output: [0,6]
// Explanation:
// The substring with start index = 0 is "cba", which is an anagram of "abc".
// The substring with start index = 6 is "bac", which is an anagram of "abc".
// Example 2:

// Input: s = "abab", p = "ab"
// Output: [0,1,2]
// Explanation:
// The substring with start index = 0 is "ab", which is an anagram of "ab".
// The substring with start index = 1 is "ba", which is an anagram of "ab".
// The substring with start index = 2 is "ab", which is an anagram of "ab".
 

// Constraints:

// 1 <= s.length, p.length <= 3 * 104
// s and p consist of lowercase English letters.

/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    let res = [];
    let map = new Array(26).fill(0);
    for (let i = 0; i < p.length; i++) {
        map[p.charCodeAt(i) - 97]++;
    }
    let left = 0;
    let right = 0;
    let count = p.length;
    while (right < s.length) {
        if (map[s.charCodeAt(right++) - 97]-- >= 1) {
            count--;
        }
        if (count === 0) {
            res.push(left);
        }
        if (right - left === p.length && map[s.charCodeAt(left++) - 97]++ >= 0) {
            count++;
        }
    }
    return res;
};
// The solution uses a sliding window approach with two pointers, left and right. The algorithm uses a map to store the count of each character in the target string p, and decrements the count of each character in the map when it is found in the sliding window. If the count of a character becomes zero, it means the current sliding window contains an anagram of the target string. The left pointer moves to the right if the window size exceeds the length of the target string, and increments the count of the character that is removed from the window in the map. The algorithm continues until the right pointer reaches the end of the string.