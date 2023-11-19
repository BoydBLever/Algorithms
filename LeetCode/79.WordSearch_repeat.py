class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(board, word, index, r, c):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'  # Marking the cell as visited

            found = (backtrack(board, word, index + 1, r + 1, c) or
                     backtrack(board, word, index + 1, r - 1, c) or
                     backtrack(board, word, index + 1, r, c + 1) or
                     backtrack(board, word, index + 1, r, c - 1))

            board[r][c] = temp  # Restore the cell's original value (backtrack)
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
               if board[i][j] == word[0] and backtrack(board, word, 0, i, j):
                   return True
        return False