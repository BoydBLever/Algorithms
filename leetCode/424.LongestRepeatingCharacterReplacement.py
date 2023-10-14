# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Step 1: Initialize variables
        start, end, max_length, max_count = 0, 0, 0, 0
        char_freq = [0] * 26  # Since s consists of only uppercase English letters
        
        # Step 2: Slide the window
        while end < len(s):
            # Update the frequency count of the current character
            char_freq[ord(s[end]) - ord('A')] += 1
            # Update max_count with the most frequent character's count
            max_count = max(max_count, char_freq[ord(s[end]) - ord('A')])
            
            # If characters that need to be changed > k, shrink window from the left
            if (end - start + 1) - max_count > k:
                char_freq[ord(s[start]) - ord('A')] -= 1
                start += 1
            
            # Update max_length
            max_length = max(max_length, end - start + 1)
            end += 1
        
        # Step 3: Return result
        return max_length

#Neetcode solution
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = {}
#         res = 0

#         l = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)

#             while (r - l + 1) - max(count.values()) > k:
#                 count[s[l]] -= 1
#                 l += 1

#             res = max(res, r - l + 1)
#         return res