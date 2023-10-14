/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 *
 * Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
 * Return all such possible sentences in any order.
 * 
 * Note that the same word in the dictionary may be reused multiple times in the segmentation.
 * 
 * https://leetcode.com/problems/word-break-ii/
 */

const string1 = "catsanddog"
const word1 = ["cat", "cats", "and", "sand", "dog"]
const expect1 = ["cats and dog", "cat sand dog"]

const string2 = "pineapplepenapple"
const word2 = ["apple", "pen", "applepen", "pine", "pineapple"]
const expect2 = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
// Explanation: Note that you are allowed to reuse a dictionary word.

const string3 = "catsandog"
const word3 = ["cats", "dog", "sand", "and", "cat"]
const expect3 = []
// const wordBreakLVL2 = (s, wordDict) => {
// };
function wordBreak(s, wordDict) {
    const wordSet = new Set(wordDict);
    const n = s.length;
    const dp = Array(n + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            if (dp[j] && wordSet.has(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }

    const results = [];
    const path = [];
    if (dp[n]) {
        dfs(s, wordSet, dp, 0, path, results);
    }

    return results;
}

function dfs(s, wordSet, dp, start, path, results) {
    if (start === s.length) {
        results.push(path.join(" "));
        return;
    }

    for (let end = start + 1; end <= s.length; end++) {
        if (dp[end] && wordSet.has(s.substring(start, end))) {
            path.push(s.substring(start, end));
            dfs(s, wordSet, dp, end, path, results);
            path.pop();
        }
    }
}


console.log(wordBreakLVL2(string1, word1))
console.log(wordBreakLVL2(string2, word2))
console.log(wordBreakLVL2(string3, word3))