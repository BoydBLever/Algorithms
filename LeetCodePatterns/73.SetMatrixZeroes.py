class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Initialize variables
        firstRowZero = False
        firstColZero = False
        
        # Step 2: Set flags for first row and first column
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                firstRowZero = True
                break
        
        # Step 3: Mark zeros in the rest of the matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 4: Set zeros based on flags
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRowZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if firstColZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0