class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 1. Matrix Transposition : swap the elements across the diagonal which is from top left to bottom right. It turns rows into columns.
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Reverse the order of the elements in each row of the matrix
        for i in range(n):
            matrix[i].reverse()

# 1 2 3
# 4 5 6
# 7 8 9
# After Transposition: the first row becomes the first column and so on.
# 1 4 7
# 2 5 8
# 3 6 9
# After Reverse of each element in reach row:
# 7 4 1
# 8 5 2
# 9 6 3 
for i in range(n): # this loop iterates over each row of the matrix with i as the row index
    for j in range(i, n): # iterate over each column of the matrix with j as the column index. i is the row index, so j starts from i. n is the length of the matrix.
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # This swapping effectively flips the element positions across the main diagonal (top-left to bottom-right) of the matrix.
    # The key here is the starting point of the inner loop, which avoids re-swapping elements that have already been swapped in earlier iterations.