// // Maze parameters
// const width = 20;
// const height = 20;
// const start = [0, 0];
// const end = [width - 1, height - 1];

// // Create an empty maze
// const maze = new Array(height);
// for (let i = 0; i < height; i++) {
//   maze[i] = new Array(width).fill(1);
// }

// // Generate a random maze using depth-first search
// const stack = [start];
// while (stack.length > 0) {
//   const [x, y] = stack.pop();
//   maze[y][x] = 0;
//   const neighbors = getNeighbors(x, y, maze);
//   if (neighbors.length > 0) {
//     stack.push([x, y]);
//     const [nx, ny] = neighbors[Math.floor(Math.random() * neighbors.length)];
//     removeWall(x, y, nx, ny, maze);
//     stack.push([nx, ny]);
//   }
// }

// // Print the maze to the console
// // console.log(maze);
// let output = "";
// for (let y = 0; y < height; y++) {
//   for (let x = 0; x < width; x++) {
//     output += maze[y][x] === 1 ? "#" : " ";
//   }
//   output += "\n";
// }
// console.log(output);


// // Solve the maze using depth-first search
// const visited = new Set();
// const path = dfs(start, end, maze, visited);
// console.log(path);

// // Helper functions
// function getNeighbors(x, y, maze) {
//   const neighbors = [];
//   if (x > 0 && maze[y][x - 1] === 1) neighbors.push([x - 1, y]);
//   if (x < width - 1 && maze[y][x + 1] === 1) neighbors.push([x + 1, y]);
//   if (y > 0 && maze[y - 1][x] === 1) neighbors.push([x, y - 1]);
//   if (y < height - 1 && maze[y + 1][x] === 1) neighbors.push([x, y + 1]);
//   return neighbors;
// }

// function removeWall(x1, y1, x2, y2, maze) {
//   if (x1 === x2) {
//     if (y1 < y2) maze[y1 + 1][x1] = 0;
//     else maze[y1 - 1][x1] = 0;
//   } else {
//     if (x1 < x2) maze[y1][x1 + 1] = 0;
//     else maze[y1][x1 - 1] = 0;
//   }
// }

// function dfs(current, target, maze, visited) {
//   if (current[0] === target[0] && current[1] === target[1]) {
//     return [current];
//   }
//   visited.add(current.toString());
//   const neighbors = getNeighbors(current[0], current[1], maze);
//   for (const neighbor of neighbors) {
//     if (!visited.has(neighbor.toString())) {
//       const path = dfs(neighbor, target, maze, visited);
//       if (path !== null) {
//         path.unshift(current);
//         return path;
//       }
//     }
//   }
//   return null;
// }
// // Print the maze as a string of characters
// Maze parameters
const width = 20;
const height = 20;
const start = [0, 0];
const end = [width - 1, height - 1];

// Create an empty maze
const maze = new Array(height);
for (let i = 0; i < height; i++) {
  maze[i] = new Array(width).fill(1);
}

// Generate a random maze using depth-first search
const stack = [start];
while (stack.length > 0) {
  const [x, y] = stack.pop();
  maze[y][x] = 0;
  const neighbors = getNeighbors(x, y, maze);
  if (neighbors.length > 0) {
    stack.push([x, y]);
    const [nx, ny] = neighbors[Math.floor(Math.random() * neighbors.length)];
    removeWall(x, y, nx, ny, maze);
    stack.push([nx, ny]);
  }
}

// Print the maze to the console
let output = "";
for (let y = 0; y < height; y++) {
  for (let x = 0; x < width; x++) {
    output += maze[y][x] === 1 ? "#" : " ";
  }
  output += "\n";
}
console.log(output);

// Solve the maze using depth-first search
const visited = new Set();
const path = dfs(start, end, maze, visited);
console.log(path);

// Helper functions
function getNeighbors(x, y, maze) {
  const neighbors = [];
  if (x > 0 && maze[y][x - 1] === 1) neighbors.push([x - 1, y]);
  if (x < width - 1 && maze[y][x + 1] === 1) neighbors.push([x + 1, y]);
  if (y > 0 && maze[y - 1][x] === 1) neighbors.push([x, y - 1]);
  if (y < height - 1 && maze[y + 1][x] === 1) neighbors.push([x, y + 1]);
  return neighbors;
}

function removeWall(x1, y1, x2, y2, maze) {
  if (x1 === x2) {
    if (y1 < y2) maze[y1 + 1][x1] = 0;
    else maze[y1 - 1][x1] = 0;
  } else {
    if (x1 < x2) maze[y1][x1 + 1] = 0;
    else maze[y1][x1 - 1] = 0;
  }
}

function dfs(current, target, maze, visited) {
  if (current[0] === target[0] && current[1] === target[1]) {
    return [current];
  }
  visited.add(current.toString());
  const neighbors = getNeighbors(current[0], current[1], maze);
  for (const neighbor of neighbors) {
    if (!visited.has(neighbor.toString())) {
      const path = dfs(neighbor, target, maze, visited);
      if (path !== null) {
        path.unshift(current);
        return path;
      }
    }
  }
  return null;
}
