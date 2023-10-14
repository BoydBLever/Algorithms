// https://leetcode.com/problems/longest-palindromic-substring/submissions/901351116/?envType=study-plan&id=algorithm-ii

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    const n = s.length;
    let dp = Array(n).fill().map(() => Array(n).fill(false));
    let maxLength = 1;
    let start = 0;

    // mark single characters as palindrome
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
    }

    // check for palindromes of length 2
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === s[i + 1]) {
            dp[i][i + 1] = true;
            maxLength = 2;
            start = i;
        }
    }

    // check for palindromes of length 3 and above
    for (let len = 3; len <= n; len++) {
        for (let i = 0; i < n - len + 1; i++) {
            let j = i + len - 1;
            if (dp[i + 1][j - 1] && s[i] === s[j]) {
                dp[i][j] = true;
                if (len > maxLength) {
                    maxLength = len;
                    start = i;
                }
            }
        }
    }

    return s.substring(start, start + maxLength);
};