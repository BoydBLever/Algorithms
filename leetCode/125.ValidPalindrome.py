# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase.
        s = s.lower()
        
        # Filter out non-alphanumeric characters from the string.
        filtered_s = ''.join(ch for ch in s if ch.isalnum())
        
        # Check if the filtered string is equal to its reverse.
        return filtered_s == filtered_s[::-1]

# Testing the function on given examples
test_cases_4 = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True)
]

results_4 = [(test[0], Solution().isPalindrome(test[0]) == test[1]) for test in test_cases_4]
results_4
#Neetcode solution (ignores cases so not all letters are converted to lowercase since the problem statement appears slighltly different for 125 on Leetcode versus the Neetcode solution as of Oct 13 2023)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         Solution 1
#         newString = ""

#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]
    
#         Solution 2
#         Use Two Pointers
#     def isPalindrome(self, s: str) -> bool:
#         1, r = 0, len(s) - 1

#         while 1 < r:
#             while 1 < r and not self.alphaNum(s[1]):
#                 l += 1
#             while r > 1 and not self.alphaNum(s[r]):
#                 r -= 1
#             if s[1].lower() != s[r].lower():
#                 return False
#             l, r = 1 + 1, r - 1
#         return True
    
#     def alphaNum(self, c):
#         return (ord('A') <= ord(c) <= ord   ('Z') or 
#             ord('a') <= ord(c) <= ord('z') or
#             ord('0') <= ord(c) <= ord('9'))
