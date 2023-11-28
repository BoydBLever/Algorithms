# https://leetcode.com/problems/palindrome-partitioning/description/
# NeetCode solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPali(self, s, l r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r -1
        return True
    # Time Complexity: O(n * 2^n)
# Decision Tree for s = "aab"
#               "" // This is the root of the tree, where no decisions have been made
#                |
#              ("a") // Loop starts at i = 0, which is "a". Since "a" is a palindrome, we apped it to the current partition, and make a recursive call with dfs(j + 1), which is equivalent to exploring the left branch leading to "a" in the tree. After the recursive call, part.pop() removes "a", backtracking to try the next possibility. Exploring "aa". The next iteration in the loop appends "aa" to part, since it is a palindrome and calls dfs(j + 1), corresponding to the right branch "aa". Part.pop() removes "aa", the algo backtracks to try other possibilities.         
#              ___|____________
#             /                \
#        ("a", "a")             ("aa")     
#          /       \              |
# ("a", "a", "b") ("a", "ab") ("aa", "b")
#                      X           

# Another Completed Decision Tree for s = "aab"
#              ""
#               |
#              "a"             
#             /   \
#           "a"   "aa"         
#          /   \      \
#       "a|a" "a|ab" "aa|b"   
#        /       X      |
#    "a|a|b"           "aa|b"

# Decision Tree for s = "bba"
#              ""
#               |
#              "b"             
#             /   \
#         "b"     "bb"         
#        /   \      \
#     "b|b" "b|ba" "bb|a"  "bba"
#      /      X     /        X
# "b|b|a"        "bb|a"