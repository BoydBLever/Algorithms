class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan&id=algorithm-ii
# We start by checking if the matrix is empty. If it is, we return False because the target cannot be found in the matrix.

# Next, we use binary search to find the index of the target in the flattened matrix. We initialize the left and right indices to 0 and m * n - 1, respectively, where m is the number of rows in the matrix and n is the number of columns. We use the formula mid = (left + right) // 2 to calculate the middle index of the current range, and we use the divmod function to convert the 1D index to the corresponding row and column indices in the 2D matrix.

# If the value at the middle index is equal to the target, we return True. If the value is less than the target, we narrow down the search range by setting the left index to mid + 1. Otherwise, we narrow down the search range by setting the right index to mid - 1.

# If we couldn't find the target during the binary search, we return False as the output.

# This algorithm has a time complexity of O(log(m * n)) because we use binary search to search through a flattened version of the matrix that has m * n elements.