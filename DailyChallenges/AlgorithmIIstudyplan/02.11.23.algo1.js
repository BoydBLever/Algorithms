// https://leetcode.com/problems/number-of-islands/?envType=study-plan&id=algorithm-ii
// Given an m x n 2D binary grid grid which represents a map of '1's(land) and '0's(water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.You may assume all four edges of the grid are all surrounded by water.

//     Example 1:

// Input: grid = [
//     ["1", "1", "1", "1", "0"],
//     ["1", "1", "0", "1", "0"],
//     ["1", "1", "0", "0", "0"],
//     ["0", "0", "0", "0", "0"]
// ]
// Output: 1
// Example 2:

// Input: grid = [
//     ["1", "1", "0", "0", "0"],
//     ["1", "1", "0", "0", "0"],
//     ["0", "0", "1", "0", "0"],
//     ["0", "0", "0", "1", "1"]
// ]
// Output: 3

// Constraints:

// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 300
// grid[i][j] is '0' or '1'.
/**
 * @param {character[][]} grid
 * @return {number}
 */
function numIslands(grid) {
    if (!grid || !grid.length) return 0;

    const m = grid.length;
    const n = grid[0].length;
    let count = 0;

    const dfs = (i, j) => {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] === '0') return;

        grid[i][j] = '0';
        dfs(i - 1, j);
        dfs(i + 1, j);
        dfs(i, j - 1);
        dfs(i, j + 1);
    };

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === '1') {
                count++;
                dfs(i, j);
            }
        }
    }

    return count;
}
// You can solve this problem using a Depth First Search (DFS) algorithm. In this solution, the dfs function is used to traverse the grid and mark connected land cells as '0' (water). The count variable is used to keep track of the number of islands. The outer loop iterates through each cell in the grid, and if it is a '1' (land), the dfs function is called and the count is incremented. This way, we can ensure that each connected component of land cells is counted as a single island.