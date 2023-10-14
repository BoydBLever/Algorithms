// https://leetcode.com/problems/construct-quad-tree/submissions/905664084/
/**
 * // Definition for a QuadTree node.
 * function Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {number[][]} grid
 * @return {Node}
 */
var construct = function(grid) {
    const n = grid.length;
    if (n === 1) {
        return new Node(grid[0][0] === 1, true, null, null, null, null);
    }
    const isLeaf = checkIsLeaf(grid);
    if (isLeaf !== null) {
        return new Node(isLeaf, true, null, null, null, null);
    }
    const half = n >> 1;
    const topLeft = construct(getSubGrid(grid, 0, 0, half));
    const topRight = construct(getSubGrid(grid, 0, half, half));
    const bottomLeft = construct(getSubGrid(grid, half, 0, half));
    const bottomRight = construct(getSubGrid(grid, half, half, half));
    return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
};

function checkIsLeaf(grid) {
    const first = grid[0][0];
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] !== first) {
                return null;
            }
        }
    }
    return first === 1;
}

function getSubGrid(grid, rowStart, colStart, size) {
    const subGrid = new Array(size);
    for (let i = 0; i < size; i++) {
        subGrid[i] = grid[rowStart + i].slice(colStart, colStart + size);
    }
    return subGrid;
}

// The construct function takes a grid as input and returns the root of the corresponding Quad-Tree. It first checks whether the grid is a single cell, in which case it creates a leaf node with the appropriate value. If the grid is not a leaf, it checks whether all its values are the same, in which case it creates a leaf node with the appropriate value. If the grid is neither a single cell nor a leaf, it divides the grid into four sub-grids and recursively constructs the Quad-Tree for each sub-grid. Finally, it returns a non-leaf node with the four sub-trees as its children.

// The checkIsLeaf function takes a grid as input and checks whether all its values are the same. If they are, it returns the appropriate value (either true or false), otherwise it returns null.

// The getSubGrid function takes a grid, a starting row and column index (rowStart and colStart, respectively), and a size, and returns a new grid that is a sub-grid of the original grid starting at the specified row and column and with the specified size.