// https://leetcode.com/problems/subarray-product-less-than-k/?envType=study-plan&id=algorithm-ii
// Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

// Example 1:

// Input: nums = [10,5,2,6], k = 100
// Output: 8
// Explanation: The 8 subarrays that have product less than 100 are:
// [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
// Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
// Example 2:

// Input: nums = [1,2,3], k = 0
// Output: 0

// Constraints:

// 1 <= nums.length <= 3 * 104
// 1 <= nums[i] <= 1000
// 0 <= k <= 106
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let res = 0;
    let left = 0;
    let prod = 1;
    for (let right = 0; right < nums.length; right++) {
        prod *= nums[right];
        while (prod >= k && left <= right) {
            prod /= nums[left++];
        }
        res += right - left + 1;
    }
    return res;
};
// The solution uses two pointers, left and right, and a variable prod to store the product of the elements in the subarray. The algorithm starts from the left pointer and adds the right pointer until the product is less than k. If the product becomes greater than or equal to k, the algorithm removes the left pointer until the product is less than k again. The algorithm continues until the right pointer reaches the end of the array, and the result is the number of contiguous subarrays where the product of all the elements is less than k.