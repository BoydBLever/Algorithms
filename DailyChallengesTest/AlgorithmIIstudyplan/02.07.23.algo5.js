//https://leetcode.com/problems/find-peak-element/?envType=study-plan&id=algorithm-ii
// One way to solve this problem in O(log n) time is to use binary search. The idea is to find the middle element, compare it with its neighbors, and decide whether the peak is in the left half or the right half of the array.

// Here's one possible implementation in JavaScript:

function findPeakElement(nums) {
    let low = 0;
    let high = nums.length - 1;
    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        if (nums[mid] < nums[mid + 1]) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}

// In this solution, low and high are used to keep track of the start and end indices of the subarray being searched. The variable mid is the middle index of the subarray. If nums[mid] < nums[mid + 1], it means that the peak is in the right half of the array, so we update low to mid + 1. Otherwise, the peak is in the left half of the array, so we update high to mid.
