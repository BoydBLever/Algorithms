// https://leetcode.com/problems/two-sum/
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = new Map();
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
};

// We create a map to store the elements of the array and their indices.
// For each element in the array, we calculate the complement that is needed to reach the target.
// If the complement is already in the map, we return the indices of the complement and the current element.
// If the complement is not in the map, we add the current element and its index to the map.
// This solution has a time complexity of O(n) as we need to iterate through the array only once. The space complexity is O(n) as we need to store the elements and their indices in the map.

// In the two-sum solution, the map object is used to store the elements of the array and their indices.

// The purpose of the map is to allow us to efficiently look up the indices of elements in the array that are needed to reach the target sum.

// Here's how the map is used in the solution:

// For each element in the array, we calculate the complement that is needed to reach the target.
// If the complement is already in the map, we return the indices of the complement and the current element.
// If the complement is not in the map, we add the current element and its index to the map using the set method.
// The map allows us to look up the indices of elements in constant time using the get method, which makes the solution efficient for arrays of large size.

// In the context of the two-sum problem, the complement of an element is the value that, when added to that element, results in the target sum.

// For example, given an array nums = [2, 7, 11, 15] and a target sum of 9, the complement of the element 2 is 7, because 2 + 7 = 9. The complement of the element 7 is 2, because 7 + 2 = 9.

// In the solution to the two-sum problem, the complement is calculated for each element in the array as complement = target - nums[i], where nums[i] is the current element and target is the target sum. The goal is to find two elements in the array such that their sum is equal to the target sum, which is equivalent to finding two elements in the array such that one of them is the complement of the other.