// https://leetcode.com/problems/number-of-provinces/?envType=study-plan&id=algorithm-ii
// There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

// A province is a group of directly or indirectly connected cities and no other cities outside of the group.

// You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

// Return the total number of provinces.

// Example 1:


// Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
// Output: 2
// Example 2:


// Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
// Output: 3
 

// Constraints:

// 1 <= n <= 200
// n == isConnected.length
// n == isConnected[i].length
// isConnected[i][j] is 1 or 0.
// isConnected[i][i] == 1
// isConnected[i][j] == isConnected[j][i]

// You can solve this problem using a Depth First Search (DFS) algorithm. 

function numProvinces(isConnected) {
    if (!isConnected || !isConnected.length) return 0;
  
    const n = isConnected.length;
    let count = 0;
  
    const dfs = (i, visited) => {
      for (let j = 0; j < n; j++) {
        if (isConnected[i][j] === 1 && !visited[j]) {
          visited[j] = true;
          dfs(j, visited);
        }
      }
    };
  
    const visited = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        count++;
        visited[i] = true;
        dfs(i, visited);
      }
    }
  
    return count;
  }
  
//   In this solution, the dfs function is used to traverse the graph and mark visited cities. The count variable is used to keep track of the number of provinces. The outer loop iterates through each city, and if it hasn't been visited, the dfs function is called and the count is incremented. This way, we can ensure that each connected component of cities is counted as a single province.