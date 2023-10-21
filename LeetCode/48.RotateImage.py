# Modified NeetCode solution
# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # Save the top left
                topLeft = matrix[top][l + i]

                # Move top left -> top right
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move top right -> bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move bottom right -> bottom left
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move bottom left -> top left
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1