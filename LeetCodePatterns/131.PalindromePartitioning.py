class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substring):
            return substring == substring[::-1]

        # The main backtracking function, start indicates the starting index for the next substring to consider, and path is the current list of palindromic substrings
        def backtrack(start, path):
            # If we've reached the end of the string, add the current partition to the results
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                # Check if the substring is a palindrome
                if isPalindrome(s[start:end]):
                    # If it is, include it in the current partition and continue
                    backtrack(end, path + [s[start:end]])

        res = []
        backtrack(0, [])
        return res
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)

#NeetCode solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
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
#               ""
#                |
#              ("a")           (First character, always a palindrome)
#                |
#             /     \
#        ("a", "a") ("aa")     (Two choices: Partition after 'a' or don't)
#          /          |
# ("a", "a", "b")  ("aa", "b") (For each choice, continue partitioning or not)

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