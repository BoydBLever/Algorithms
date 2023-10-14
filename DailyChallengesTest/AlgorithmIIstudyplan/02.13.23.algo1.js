// https://leetcode.com/problems/shortest-path-in-binary-matrix/solutions/3183461/javascript-optimized-shortest-path/
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {
    const n = grid.length;
    if (grid[0][0] !== 0 || grid[n-1][n-1] !== 0) {
        return -1; // If the start or end point is blocked, no clear path exists
    }
    const visited = new Set(['0,0']); // Keep track of visited cells
    const queue = [[0, 0, 1]]; // Initialize the queue with the start cell and path length
    const dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]; // 8-directional neighbors
    while (queue.length > 0) {
        const [x, y, pathLength] = queue.shift();
        if (x === n-1 && y === n-1) {
            return pathLength; // Found the end point
        }
        for (const [dx, dy] of dirs) {
            const newX = x + dx;
            const newY = y + dy;
            const key = `${newX},${newY}`;
            if (newX >= 0 && newX < n && newY >= 0 && newY < n && grid[newX][newY] === 0 && !visited.has(key)) {
                visited.add(key);
                queue.push([newX, newY, pathLength+1]);
            }
        }
    }
    return -1; // No clear path found
};