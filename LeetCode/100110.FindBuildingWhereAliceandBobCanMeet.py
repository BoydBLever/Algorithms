from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        # Precompute the max height to the left and right of each building
        max_left = [0] * n
        max_right = [0] * n
        
        max_height = heights[0]
        for i in range(n):
            max_height = max(max_height, heights[i])
            max_left[i] = max_height
        
        max_height = heights[-1]
        for i in range(n-1, -1, -1):
            max_height = max(max_height, heights[i])
            max_right[i] = max_height
        
        answer = []
        # Process each query
        for a, b in queries:
            # Initialize the leftmost building index to -1
            leftmost_building = -1
            # If Alice and Bob are at the same building, they can meet there
            if a == b:
                leftmost_building = a
            else:
                # If Alice is to the left of Bob, we look for the leftmost building
                # where the max height on Alice's path is less than or equal to the max height on Bob's path
                if a < b:
                    for i in range(a, b+1):
                        if max_left[i] <= heights[a] and max_right[i] <= heights[b]:
                            leftmost_building = i
                            break
                # If Alice is to the right of Bob, we look for the leftmost building
                # on the path from Bob to Alice with the same criteria
                else:
                    for i in range(b, a+1):
                        if max_left[i] <= heights[b] and max_right[i] <= heights[a]:
                            leftmost_building = i
                            break
            # Add the result for this query to the answer list
            answer.append(leftmost_building)
        return answer

# Create an instance of the Solution class
sol = Solution()

# Example queries
heights = [6,4,8,5,2,7]
queries = [[0,1], [0,3], [2,4], [3,1], [2,2]]

# Get the answers
print(sol.leftmostBuildingQueries(heights, queries))  # Expected output: [2,5,-1,5,2]
