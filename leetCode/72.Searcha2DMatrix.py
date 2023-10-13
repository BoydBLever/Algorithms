# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # If the matrix is empty, return False as the target cannot be found
        if not matrix or not matrix[0]:
            return False
        
        # Get the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize two pointers for binary search: start at the beginning and end at the end of the matrix
        start, end = 0, rows * cols - 1
        
        # Continue the search while start pointer is less than or equal to the end pointer
        while start <= end:
            # Calculate the middle index
            mid = (start + end) // 2
            
            # Convert the mid index to row and column indices
            row = mid // cols
            col = mid % cols
            
            # If the target is found, return True
            if matrix[row][col] == target:
                return True
            # If the target is greater than the element at the middle index, move the start pointer to mid + 1
            elif matrix[row][col] < target:
                start = mid + 1
            # If the target is less than the element at the middle index, move the end pointer to mid - 1
            else:
                end = mid - 1
        
        # If the target is not found in the matrix, return False
        return False

# Testing the function on given examples
test_cases_10 = [
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False)
]

results_10 = [(test[:-1], Solution().searchMatrix(*test[:-1]) == test[-1]) for test in test_cases_10]
results_10

#Neetcode solution
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         ROWS, COLS = len(matrix), len(matrix[0])

#     top, bot = 0, ROWS - 1
#     while top <= bot:
#         row = (top + bot) // 2
#         if target > matrix[row][-1]:
#             top = row + 1
#         elif target < matrix[row][0]:
#             bot = row - 1
#         else:
#             break
    
#     if not (top <= bot):
#         return False
#     row = (top + bot) // 2
#     l, r = 0, COLS - 1
#     while l <= r:
#         m = (l + r) // 2
#         if target > matrix[row][m]:
#             l = m + 1
#         elif target < matrix[row][m]:
#             r = m - 1
#         else:
#             return True
#      return False