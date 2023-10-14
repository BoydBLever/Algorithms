// https://leetcode.com/problems/jump-game-ii/submissions/901023458/?envType=study-plan&id=algorithm-ii
// One possible solution to this problem is to use the greedy algorithm. The basic idea is to always choose the jump that can reach the farthest position. Let's say we are at index i, and we can jump to any position between i+1 and i+nums[i]. We can calculate the farthest position we can reach from these positions, and choose the one that can reach the farthest.

// The algorithm can be implemented in the following way:
/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let n = nums.length;
    let jumps = 0;
    let currentEnd = 0;
    let farthestEnd = 0;
    
    for (let i = 0; i < n-1; i++) {
        farthestEnd = Math.max(farthestEnd, i+nums[i]);
        if (i == currentEnd) {
            jumps++;
            currentEnd = farthestEnd;
        }
    }
    
    return jumps;
};

// We initialize jumps to 0, currentEnd to 0, and farthestEnd to 0. We iterate through the array from index 0 to n-2. For each index i, we calculate the farthest position we can reach, which is i+nums[i]. We update farthestEnd to the maximum of its current value and the new farthest position. If we have reached the current end of the previous jump, which is currentEnd, we need to make a new jump. We update currentEnd to the new farthest position, and increase jumps by 1.

// After the loop, we have made the minimum number of jumps to reach the end of the array, which is n-1. We return jumps as the result.

// The time complexity of this algorithm is O(n), where n is the length of the array. The space complexity is O(1), since we only use a constant amount of extra space for storing jumps, currentEnd, and farthestEnd.