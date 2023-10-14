

var findNumberOfLIS = function(nums) {
    const n = nums.length;
    const dp = new Array(n).fill(1); // Initialize dp array with all 1's
    const count = new Array(n).fill(1); // Initialize count array with all 1's
    let maxLen = 1, ans = 0;
    
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                if (dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1; // Update dp[i]
                    count[i] = count[j]; // Update count[i]
                } else if (dp[j] + 1 === dp[i]) {
                    count[i] += count[j]; // Add count[j] to count[i]
                }
            }
        }
        maxLen = Math.max(maxLen, dp[i]); // Update maxLen
    }
    
    for (let i = 0; i < n; i++) {
        if (dp[i] === maxLen) {
            ans += count[i]; // Sum the counts of the longest increasing subsequences
        }
    }
    
    return ans;
};

// https://leetcode.com/problems/number-of-longest-increasing-subsequence/submissions/903053305/?envType=study-plan&id=algorithm-ii
// To solve this problem, we can use dynamic programming to find the length of the longest increasing subsequence that ends at each index of the nums array, and the number of such subsequences. We can create two arrays dp and count of the same length as nums, where dp[i] represents the length of the longest increasing subsequence that ends at index i, and count[i] represents the number of such subsequences. We can initialize both arrays with all 1's, since the longest increasing subsequence that ends at index i is at least the element nums[i] itself, and the number of such subsequences is also 1. Then, for each index i from 1 to n-1, we can iterate over all the previous indices j from 0 to i-1, and update dp[i] and count[i] if nums[i] is greater than nums[j]. If dp[j] + 1 is greater than dp[i], we can update dp[i] to dp[j] + 1, and set count[i] to count[j]. If dp[j] + 1 is equal to dp[i], we can add count[j] to count[i]. Finally, we can find the maximum value in the dp array, and sum the corresponding values in the count array.

// We start by initializing the dp and count arrays with all 1's. Then, we loop through the nums array from index 1 to n-1, and for each index i, we loop through all the previous indices j from 0 to i-1, and update dp[i] and count[i] if nums[i] is greater than nums[j]. If dp[j] + 1 is greater than dp[i], we update dp[i] to dp[j] + 1, since we can extend the longest increasing subsequence that ends at index j with the element nums[i] to form a longer increasing subsequence that ends at index i. We also set `count