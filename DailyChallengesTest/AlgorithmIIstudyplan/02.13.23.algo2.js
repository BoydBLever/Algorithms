// https://leetcode.com/problems/surrounded-regions/?envType=study-plan&id=algorithm-ii
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const solve = function(board) {
    const m = board.length;
    if (m === 0) {
        return;
    }
    const n = board[0].length;
    const dirs = [[-1,0],[0,-1],[1,0],[0,1]]; // 4-directional neighbors
    // Define a DFS function to mark all unmarked 'O's that are not on the border as 'F'
    const dfs = (i, j) => {
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] !== 'O') {
            return;
        }
        board[i][j] = 'F'; // Mark the current 'O' as 'F'
        for (const [dx, dy] of dirs) {
            dfs(i+dx, j+dy); // Recursively mark all unmarked 'O's that are 4-directionally connected to the current 'O'
        }
    };
    // Mark all unmarked 'O's that are not on the border as 'F'
    for (let i = 0; i < m; i++) {
        dfs(i, 0); // First column
        dfs(i, n-1); // Last column
    }
    for (let j = 0; j < n; j++) {
        dfs(0, j); // First row
        dfs(m-1, j); // Last row
    }
    // Flip all remaining 'O's to 'X' and all 'F's to 'O'
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] === 'F') {
                board[i][j] = 'O';
            }
        }
    }
};
