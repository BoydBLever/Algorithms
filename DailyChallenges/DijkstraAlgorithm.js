class PriorityQueue {
    constructor() {
      this.elements = [];
    }
  
    enqueue(element, priority) {
      this.elements.push({element, priority});
      this.elements.sort((a, b) => a.priority - b.priority);
    }
  
    dequeue() {
      return this.elements.shift().element;
    }
  
    isEmpty() {
      return this.elements.length === 0;
    }
  }
  
  class Graph {
    constructor(vertices) {
      this.vertices = vertices;
      this.adjList = new Map();
    }
  
    addEdge(u, v, w) {
      if (!this.adjList.has(u)) {
        this.adjList.set(u, []);
      }
      this.adjList.get(u).push({v, w});
    }
  
    shortestPath(start, end) {
      const distances = new Map();
      const pq = new PriorityQueue();
      for (let i = 0; i < this.vertices; i++) {
        distances.set(i, Infinity);
      }
      distances.set(start, 0);
      pq.enqueue(start, 0);
  
      while (!pq.isEmpty()) {
        const u = pq.dequeue();
        const neighbors = this.adjList.get(u) || [];
        for (const {v, w} of neighbors) {
          const distance = distances.get(u) + w;
          if (distance < distances.get(v)) {
            distances.set(v, distance);
            pq.enqueue(v, distance);
          }
        }
      }
  
      return distances.get(end);
    }
  }
  
  const graph = new Graph(9);
  graph.addEdge(0, 1, 4);
  graph.addEdge(0, 7, 8);
  graph.addEdge(1, 2, 8);
  graph.addEdge(1, 7, 11);
  graph.addEdge(2, 3, 7);
  graph.addEdge(2, 8, 2);
  graph.addEdge(2, 5, 4);
  graph.addEdge(3, 4, 9);
  graph.addEdge(3, 5, 14);
  graph.addEdge(4, 5, 10);
  graph.addEdge(5, 6, 2);
  graph.addEdge(6, 7, 1);
  graph.addEdge(6, 8, 6);
  graph.addEdge(7, 8, 7);
  
  console.log(graph.shortestPath(0, 4));

// Expected Output:

// 28 is the shortest distance from vertex 0 to vertex 4, as calculated by Dijkstra's algorithm using the given graph.
  
//   In this example, the Graph class represents the graph of a maze, and the shortestPath method implements Dijkstra's algorithm to find the shortest path from the start vertex to the end vertex. The PriorityQueue class is used to keep track of the vertices to be processed, ordered by their distance from the start vertex. The distances are stored in a Map object.

// The example creates a graph with 9 vertices and adds edges with weights representing the cost of moving from one vertex to another. The shortestPath method initializes the distances of all vertices to infinity and sets the distance of the start vertex to 0. The method then uses a priority queue to keep track of the vertices to be processed, ordered by their distance from the start vertex. The method repeatedly extracts the vertex with the lowest distance from the priority queue, updates the distances of its neighbors if necessary, and adds the neighbors to the priority queue. This continues until the end vertex is processed or the priority queue is empty. Finally, the method returns the distance of the end vertex, which is the shortest distance from the start to the end.

// Dijkstra's algorithm is a graph search algorithm that is used to find the shortest path between two nodes in a graph. It was created by Edsger W. Dijkstra in 1956 and is named after him.

// The algorithm works by maintaining a set of nodes that have been visited and a priority queue of nodes to be processed. The priority of a node in the queue is determined by its distance from the start node. The algorithm starts at the start node, adds its neighbors to the priority queue, and sets their distances as the distance from the start node plus the weight of the edge connecting them. The algorithm then extracts the node with the smallest distance from the priority queue, marks it as visited, and repeats the process for its neighbors. The process continues until the goal node is visited or the priority queue is empty.

// Dijkstra's algorithm is guaranteed to find the shortest path in a graph with non-negative edge weights. It is commonly used for routing and navigation, as well as for solving other graph-related problems.