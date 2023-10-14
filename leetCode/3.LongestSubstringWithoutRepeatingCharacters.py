# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Step 1: Initialize variables
        start, end, max_length = 0, 0, 0
        char_set = set()
        
        # Step 2: Slide the window
        while end < len(s):
            # If the character at 'end' is not in the current window, expand the window to the right
            if s[end] not in char_set:
                char_set.add(s[end])
                max_length = max(max_length, end - start + 1)
                end += 1
            # Otherwise, shrink the window from the left
            else:
                char_set.remove(s[start])
                start += 1
        
        # Step 3: Return result
        return max_length

#Neetcode solution
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res