# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w
        
        min_score = float('inf')
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for adj, score in graph[node].items():
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                min_score = min(min_score, score)
                
        return min_score
    
#The implementation creates a defaultdict of dictionaries to represent the graph. Each key in the defaultdict represents a node in the graph and its value is a dictionary containing the adjacent nodes and their respective distances. The implementation then uses a BFS algorithm to traverse the graph starting from node 1 and keeping track of the minimum distance encountered so far.

# While traversing the graph, the implementation adds each unvisited adjacent node to a deque and marks it as visited. The minimum distance encountered so far is updated in each iteration of the for loop that iterates over the adjacent nodes of the current node.

# Finally, the implementation returns the minimum score encountered while traversing the graph, which represents the minimum possible score of a path between nodes 1 and n.