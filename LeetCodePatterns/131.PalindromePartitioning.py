class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substring):
            return substring == substring[::-1]

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
# Decision Tree for s = "aab"
#               ""
#                |
#              ("a")           (First character, always a palindrome)
#                |
#             /     \
#        ("a", "a") ("aa")     (Two choices: Partition after 'a' or don't)
#          /          |
# ("a", "a", "b")  ("aa", "b") (For each choice, continue partitioning or not)