var lengthOfLIS = function(nums) {
    const n = nums.length;
    const dp = new Array(n).fill(1); // Initialize dp array with all 1's
    let maxLen = 1;
    
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1); // Update dp[i]
            }
        }
        maxLen = Math.max(maxLen, dp[i]); // Update maxLen
    }
    
    return maxLen;
};

// https://leetcode.com/problems/longest-increasing-subsequence/submissions/903043817/?envType=study-plan&id=algorithm-ii
// To solve this problem, we can use dynamic programming. We can create an array dp where dp[i] represents the length of the longest increasing subsequence that ends at index i of the nums array. We can initialize the dp array with all 1's, since the longest increasing subsequence that ends at index i is at least the element nums[i] itself. Then, for each index i from 1 to n-1, we can iterate over all the previous indices j from 0 to i-1, and update dp[i] to the maximum of its current value and dp[j] + 1 if nums[i] is greater than nums[j]. Finally, we can return the maximum value in the dp array.

// We start by initializing the dp array with all 1's. Then, we loop through the nums array from index 1 to n-1, and for each index i, we loop through all the previous indices j from 0 to i-1, and update dp[i] if nums[i] is greater than nums[j]. We update dp[i] to the maximum of its current value and dp[j] + 1, since we can extend the longest increasing subsequence that ends at index j with the element nums[i] to form a longer increasing subsequence that ends at index i. Finally, we update maxLen to the maximum value in the dp array and return it.