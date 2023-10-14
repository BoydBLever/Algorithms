//Search a 2D Matrix: https://leetcode.com/problems/search-a-2d-matrix/submissions/892768864/?envType=study-plan&id=algorithm-ii

// You are given an m x n integer matrix matrix with the following two properties:

// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the previous row.
// Given an integer target, return true if target is in matrix or false otherwise.
// You must write a solution in JavaScript with O(log(m * n)) time complexity.

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
const searchMatrix = (matrix, target) => {
    if (matrix.length === 0 || matrix[0].length === 0) return false;

    let m = matrix.length;
    let n = matrix[0].length;

    let left = 0;
    let right = m * n - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let midValue = matrix[Math.floor(mid / n)][mid % n];
        if (midValue === target) {
            return true;
        } else if (midValue < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return false;
};
// In this implementation, we perform a binary search on the flattened version of the matrix, treating it as a single sorted list. The binary search algorithm has a runtime complexity of O(log n), where n is the number of elements in the flattened matrix. So the overall time complexity is O(log(m * n)).