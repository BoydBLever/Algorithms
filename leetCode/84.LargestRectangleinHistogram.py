# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Create an empty stack to store indices of histogram bars.
        stack = []
        # Initialize max area as 0.
        max_area = 0
        
        # Iterate over the list of bar heights.
        for i in range(len(heights)):
            # Check if the stack is not empty and the current height is less than or equal to the height at the index at the top of the stack.
            while stack and heights[i] <= heights[stack[-1]]:
                # Pop the index from the stack.
                height = heights[stack.pop()]
                # Calculate width of the rectangle.
                width = i if not stack else i - stack[-1] - 1
                # Update the max area.
                max_area = max(max_area, height * width)
            # Push the current index onto the stack.
            stack.append(i)
        
        # Check remaining bars in the stack.
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area

# Testing the function on given examples
test_cases_3 = [
    ([2,1,5,6,2,3], 10),
    ([2,4], 4)
]

results_3 = [(test[0], Solution().largestRectangleArea(test[0]) == test[1]) for test in test_cases_3]
results_3

#Neetcode solution
# def largestRectangleArea(self, heights: List[int]) -> int:
#     maxArea = 0
#     stack = [] #pair: (index, height)

#     for i, h in enumerate(heights):
#         start = i
#         while stack and stack[-1][1] > h:
#             index, height = stack.pop()
#             maxArea = max(maxArea, height * (i - index))
#             start = index
#         stack.append((start, h))

#     for i, h in stack:
#         maxArea = max(maxArea, * (len(heights)- i))
#     return maxArea