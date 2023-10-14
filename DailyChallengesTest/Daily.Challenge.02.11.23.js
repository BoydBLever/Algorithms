// https://leetcode.com/problems/shortest-path-with-alternating-colors/
// You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

// You are given two arrays redEdges and blueEdges where:

// redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
// blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
// Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.



// Example 1:

// Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
// Output: [0,1,-1]
// Example 2:

// Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
// Output: [0,1,-1]


// Constraints:

// 1 <= n <= 100
// 0 <= redEdges.length, blueEdges.length <= 400
// redEdges[i].length == blueEdges[j].length == 2
// 0 <= ai, bi, uj, vj < n

/**
 * @param {number} n
 * @param {number[][]} redEdges
 * @param {number[][]} blueEdges
 * @return {number[]}
 */
function shortestAlternatingPaths(n, red, blue) {
    const blueMap = new Map();
    for (const [origin, destination] of blue) {
        if (!blueMap.has(origin)) blueMap.set(origin, []);
        blueMap.get(origin).push(destination);
    }
    const redMap = new Map();
    for (const [origin, destination] of red) {
        if (!redMap.has(origin)) redMap.set(origin, []);
        redMap.get(origin).push(destination);
    }
    let blueQueue = [0];
    let redQueue = [0];
    const sol = new Array(n);
    let level = 0;
    const blueVisited = new Array(n);
    const redVisited = new Array(n);
    while (redQueue.length || blueQueue.length) {
        const nextBlueQueue = [];
        const nextRedQueue = [];
        for (const v of blueQueue) {
            if (sol[v] === undefined) sol[v] = level;
            if (!blueVisited[v]) {
                blueVisited[v] = 1;
                const destinations = blueMap.get(v) || [];
                for (const dest of destinations) {
                    nextRedQueue.push(dest);
                }
            }
        }
        for (const v of redQueue) {
            if (sol[v] === undefined) sol[v] = level;
            if (!redVisited[v]) {
                redVisited[v] = 1;
                const destinations = redMap.get(v) || [];
                for (const dest of destinations) {
                    nextBlueQueue.push(dest);
                }
            }
        }
        blueQueue = nextBlueQueue;
        redQueue = nextRedQueue;
        level++;
    }
    for (let i = 0; i < sol.length; i++) {
        if (sol[i] === undefined) sol[i] = -1;
    }
    return sol;
}
// This solution uses two separate BFS (Breadth-first search) algorithms, one starting from the red edges and one from the blue edges, to find the shortest alternating paths from node 0 to all other nodes. The algorithm is implemented using two separate queues, redQueue and blueQueue, to keep track of the nodes to be visited in each BFS iteration. In each iteration, the algorithm visits all nodes in the current queue and adds their unvisited neighbors to the next iteration's queue.

// The algorithm uses two separate maps, redMap and blueMap, to store the red and blue edges in an adjacency list format. This allows for quick access to the neighbors of each node during the BFS algorithm. The maps are created by looping through the redEdges and blueEdges arrays and adding each edge to the respective map.

// The algorithm uses two separate arrays, redVisited and blueVisited, to keep track of which nodes have been visited in each BFS algorithm. This ensures that a node is only visited once in each algorithm, even if it has multiple edges connecting it to the current node.

// The sol array is used to store the length of the shortest alternating path to each node. If a node is not reachable, its value in the sol array is set to -1.

// The level variable is used to keep track of the number of steps taken in each iteration of the BFS algorithm. It is incremented by 1 in each iteration. The value of level is used to set the value of sol[v] for each node v that is visited for the first time.