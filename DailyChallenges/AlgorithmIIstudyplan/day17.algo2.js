var minDistance = function(word1, word2) {
    // Define the length of the input strings.
    const m = word1.length, n = word2.length;
    
    // Create a 2D array dp with dimensions (m+1)x(n+1) and initialize it to 0.
    const dp = new Array(m+1).fill().map(() => new Array(n+1).fill(0));
    
    // Set the base cases: dp[i][0] = i for all i from 0 to m, and dp[0][j] = j for all j from 0 to n.
    for (let i = 1; i <= m; i++) {
        dp[i][0] = i;
    }
    for (let j = 1; j <= n; j++) {
        dp[0][j] = j;
    }
    
    // Fill in the rest of the array using dynamic programming.
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            // If the last characters of the two prefixes are the same, we don't need to delete any characters.
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                // Otherwise, we need to delete one character from either word1 or word2, and take the minimum of the two options.
                dp[i][j] = 1 + Math.min(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    // Return the minimum number of steps required to make the two strings the same.
    return dp[m][n];
};
// https://leetcode.com/problems/delete-operation-for-two-strings/submissions/903071338/?envType=study-plan&id=algorithm-ii
// The overall approach is to use dynamic programming to compute the minimum number of steps required to make the two strings the same. The 2D array dp stores the minimum number of steps required to make the prefix of word1 of length i and the prefix of word2 of length j the same. The base cases are dp[i][0] = i and dp[0][j] = j, since we can always make one string the same as the empty string by deleting all its characters.

// To fill in the rest of the array, we use the recurrence relation:

// dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] (i.e., the last characters of the two prefixes are the same)
// dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1]) otherwise (i.e., we need to delete one character from either word1 or word2, and take the minimum of the two options).
// Finally, the minimum number of steps required to make the two strings the same is dp[m][n].