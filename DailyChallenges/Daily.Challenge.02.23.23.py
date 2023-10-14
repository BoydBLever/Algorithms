import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        pq = [] # priority queue of capital requirements
        h = [] # heap of project profits
        i = 0
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(h, -projects[i][1])
                i += 1
            if not h:
                break
            w -= heapq.heappop(h)
            k -= 1
        return w
# https://leetcode.com/problems/ipo/description/
# Here's a step-by-step explanation of the Python implementation:

# We begin by importing the heapq module, which provides functions to implement heaps (priority queues) in Python. We also define a class Solution with a method findMaximizedCapital that takes four arguments: k, w, profits, and capital.

# We create a list of tuples projects containing the capital and profit for each project, and sort the list by capital in ascending order using the sorted function and the zip function to combine the capital and profits lists. This ensures that we can process the projects in order of increasing capital requirement.

# We initialize two data structures: a priority queue pq to keep track of the capital requirements of the projects that can be completed with the current available capital, and a heap h to keep track of the profits of the projects that can be completed with the current available capital. We also initialize a counter i to keep track of the index of the last project that has been added to the heap.

# We loop while we still have projects to complete (k > 0), and while there are projects that can be completed with the current available capital.

# Inside the loop, we add all the projects that can be started with the current available capital to the heap by iterating through the projects list and adding the profits of the projects whose capital requirements are less than or equal to w to the heap. We use the heapq.heappush function to add items to the heap, and the heapq.heappop function to remove the item with the highest profit from the heap.

# If there are no more projects that can be completed with the current available capital, we break out of the loop.

# Otherwise, we subtract the capital requirement of the project with the highest profit from the current available capital, and decrement the counter k to indicate that we have completed a project.

# Finally, we return the final value of the current available capital.

# This approach ensures that we always choose the project with the highest profit that can be completed with the current available capital, and that we process the projects in order of increasing capital requirement.