# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> bool:
        # Pseudocode:
        # 1. Iterate over the board to check each row, column, and 3x3 box.
        # 2. Use three sets for rows, columns, and boxes to store the seen numbers.
        # 3. For each number in the board, check if it's already in the corresponding set.
        # 4. If yes, return False since it's a repetition.
        # 5. Otherwise, add it to the set.
        # 6. Return True at the end if no repetitions are found.

        # Check rows
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
        
        # Check columns
        for j in range(9):
            col_set = set()
            for i in range(9):
                if board[i][j] != '.' and board[i][j] in col_set:
                    return False
                col_set.add(board[i][j])
        
        # Check 3x3 boxes
        for i in range(0, 9, 3):  # starting row index for each 3x3 box
            for j in range(0, 9, 3):  # starting column index for each 3x3 box
                box_set = set()
                for k in range(3):  # row offset within the 3x3 box
                    for l in range(3):  # column offset within the 3x3 box
                        num = board[i + k][j + l]
                        if num != '.' and num in box_set:
                            return False
                        box_set.add(num)
        
        # If no repetitions are found, the board is valid
        return True