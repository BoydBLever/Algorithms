# NeetCode solution
# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False

        # Determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    if r == 0:  # Check if first row needs to be zeroed
                        rowZero = True
                    if c == 0:  # Check if first column needs to be zeroed
                        colZero = True

        # Set the necessary rows and columns to zero, but skip the first row and column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # If necessary, set the first row to zero
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        # If necessary, set the first column to zero
        if colZero:
            for r in range(ROWS):
                matrix[r][0] = 0