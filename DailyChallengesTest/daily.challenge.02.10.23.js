https://leetcode.com/problems/as-far-from-land-as-possible/

// Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

// The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

// Example 1:

// Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
// Output: 2
// Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
// Example 2:


// Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
// Output: 4
// Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 
// Constraints:

// n == grid.length
// n == grid[i].length
// 1 <= n <= 100
// grid[i][j] is 0 or 1

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    let q = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                q.push([i, j]);
            }
        }
    }
    if (q.length === 0 || q.length === m * n) {
        return -1;
    }
    let res = 0;
    let dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    while (q.length > 0) {
        let size = q.length;
        while (size-- > 0) {
            let [x, y] = q.shift();
            for (let dir of dirs) {
                let i = x + dir[0];
                let j = y + dir[1];
                if (i >= 0 && i < m && j >= 0 && j < n && grid[i][j] === 0) {
                    grid[i][j] = 1;
                    q.push([i, j]);
                }
            }
        }
        res++;
    }
    return res - 1;
};

// The solution uses BFS to solve the problem. The algorithm first finds all the land cells in the grid and adds them to a queue. If there is no land cell or all the cells are land cells, the algorithm returns -1. The algorithm then iterates the queue, and for each cell in the queue, it adds its neighbors that are water cells to the queue, and updates the distance. The algorithm continues until the queue is empty, and the final result is the distance minus one.