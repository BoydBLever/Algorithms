

Algorithms and Data Structures for Beginners
28 / 35








































30 - Matrix BFS

Suggested Problems

Status
Star
Problem   
Difficulty   
Video Solution
Code
Shortest Path in Binary Matrix	
Rotting Oranges	
Matrix BFS
The type of graph questions where BFS will shine is usually when the question asks us to find the shortest path.

Let's dive into the question straightaway. You will notice that the code for BFS on a graph looks similar to BFS on trees, with some edge cases.

Q: Find the length of the shortest path from top left of the grid to the bottom right.
We can also use DFS to do this but it is more brute-force. BFS is more efficient since the first time a vertex is discovered during the traversal, the distance from our source would give us the shortest path. Let us see the set up of the code, given the following matrix.

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
The initial set up
Similar to the previous chapter, we take the dimensions of our row and columns, which tells us where our bounds are. We will use a set to keep track of visited vertices. We will use a deque (deck) to keep track of all visited vertices at each level and determine what level we are at currently. We can initialize our deque to the first vertex, (0, 0) and mark it as visited. This is our starting point.

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))
BFS on the graph
We are asked to find the length of the shortest path. After our initial set up, we can initialize a length variable to 0. Then, just like BFS on trees, we can run a while loop for our queue and take a snapshot of the length of the queue. Here, when we pop from our queue, we get a r (row) and c (column). With trees, the next step was to visit the children of the popped node. Here, we visit the neighbors of the popped vertex. We will only have to do this if we have not already reached the bottom right, which is when r == ROWS - 1 and c == COLS - 1.

In the best case, we might be able to move in all four directions without going out of bounds. For this, we can keep a 2-D array - neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]. Though not technically the neighbors, the array just represents the directions we can move in - right, left, up, down, respectively.

The code in the if statement is the same as what we had in DFS. If we are out of bounds, the coordinate is blocked or the vertex is already visited, we continue to the next iteration. Otherwise, we append all the neighbors to the queue and add them to the hashset to ensure we don't visit them again. Notice how we add to the hashset as soon as we append to the queue. This way, we will never have the same element occur twice in our queue, which helps in making it more efficient in time complexity, which we will discuss later. The next piece of code after the initial setup looks like this.

length = 0
while queue:
    for i in range(len(queue)):
        r, c = queue.popleft()
        if r == ROWS - 1 and c == COLS - 1:
            return length

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in neighbors:
            if (min(r + dr, c + dc) < 0 or
                r + dr == ROWS or c + dc == COLS or
                (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                continue
            queue.append((r + dr, c + dc))
            visit.add((r + dr, c + dc))
    length += 1
Tying it all together, we will end up with the following.

# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1
We can visualize this algorithm applied to our matrix below. The numbers and circles in the same color represent the length of the path at that specific vertex.

matrixbfs

Time Complexity
Since we are never visiting a coordinate twice, in the worst case, we end up visiting each coordinate at most once. If 
�
n is the number of rows and 
�
m is the number of columns, this gives us a time complexity of 
�
(
�
 
∗
 
�
)
O(n ∗ m).

from collections import deque

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1
Copyright © 2023 NeetCode.io All rights reserved.
Contact:  neetcodebusiness@gmail.com

Github    Privacy    Terms