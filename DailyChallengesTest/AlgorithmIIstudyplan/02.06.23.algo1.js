// Day 1 Binary Search
// Find First and Last Position of Element in Sorted Array: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/892761928/?envType=study-plan&id=algorithm-ii

//Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value using JavaScript code. If target is not found in the array, return [-1, -1].

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const searchRange = (nums, target) => {
    let start = -1;
    let end = -1;

    // binary search for the starting position
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (nums[mid] >= target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
        if (nums[mid] === target) {
            start = mid;
        }
    }

    // binary search for the ending position
    left = 0;
    right = nums.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
        if (nums[mid] === target) {
            end = mid;
        }
    }

    return start === -1 ? [-1, -1] : [start, end];
};
// In this implementation, we perform two binary searches: one to find the starting position and one to find the ending position. The binary search algorithm has a runtime complexity of O(log n), where n is the number of elements in the array nums.