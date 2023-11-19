class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        
        # m and n represent dimensions of the matrix (m rows and n columns)
        m, n = len(matrix), len(matrix[0])
        # Define the boundaries of the current layer of the spiral
        top, bottom, left, right = 0, m - 1, 0, n - 1
        # Spiral Traversal continues as long as top is less than or equal to bottom, and left is less than or equal to right, ensuring the traveral doesn't go out of bounds
        while top <= bottom and left <= right:
            # Traverse top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top > bottom or left > right:
                break
            
            # Traverse bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
            # Traverse left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
        return result