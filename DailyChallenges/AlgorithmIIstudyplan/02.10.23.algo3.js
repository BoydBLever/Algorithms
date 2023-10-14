// https://leetcode.com/problems/minimum-size-subarray-sum/description/

// Given an array of positive integers nums and a positive integer target, return the minimal length of a 
// subarray
//  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

// Example 1:

// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: The subarray [4,3] has the minimal length under the problem constraint.
// Example 2:

// Input: target = 4, nums = [1,4,4]
// Output: 1
// Example 3:

// Input: target = 11, nums = [1,1,1,1,1,1,1,1]
// Output: 0
 

// Constraints:

// 1 <= target <= 109
// 1 <= nums.length <= 105
// 1 <= nums[i] <= 104
/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let res = nums.length + 1;
    let left = 0;
    let sum = 0;
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum >= target) {
            res = Math.min(res, right - left + 1);
            sum -= nums[left++];
        }
    }
    return res === nums.length + 1 ? 0 : res;
};
// The solution uses two pointers, left and right, and a variable sum to store the sum of the elements in the subarray. The algorithm starts from the left pointer and adds the right pointer until the sum is greater than or equal to the target. If the sum becomes greater than or equal to the target, the algorithm removes the left pointer until the sum is less than the target again. The algorithm continues until the right pointer reaches the end of the array, and the result is the minimal length of the subarray whose sum is greater than or equal to the target.

// Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).