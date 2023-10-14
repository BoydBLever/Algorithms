# https://leetcode.com/problems/permutation-in-string/
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Step 1: Initialize variables
        start, end = 0, 0
        s1_freq = defaultdict(int)
        window_freq = defaultdict(int)
        
        # Step 2: Construct the Frequency Map for s1
        for char in s1:
            s1_freq[char] += 1
        
        # Step 3: Slide the window in s2
        while end < len(s2):
            # Update the frequency count of the current character in s2
            window_freq[s2[end]] += 1
            end += 1
            
            # If window size becomes equal to length of s1
            if end - start == len(s1):
                # Check if window_freq matches s1_freq
                if window_freq == s1_freq:
                    return True
                # Shrink the window from the left
                window_freq[s2[start]] -= 1
                if window_freq[s2[start]] == 0:
                    del window_freq[s2[start]]
                start += 1
        
        # Step 4: Return result
        return False

#Neetcode solution
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2): return False

#         s1Count, s2Count = [0] * 26, [0] * 26
#         for 1 in range(len(s1)):
#             s1Count[ord(s1[i]) - ord('a')] += 1
#             s2Count[ord(s2[i]) - ord('a')] += 1
        
#         matches = 0
#         for i in range(26):
#             matches += (1 if s1Count[i] == s2Count[i] else 0)

#         l = 0
#         for r in range(len(s1), len(s2))
#             if matches == 26: return True

#             index = ord(s2[r]) - ord('a')
#             s2Count[index] += 1
#             if s1Count[index] == s2Count[index]
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:
#                 matches -= 1

#             index = ord(s2[l]) - ord('a')
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]:
#                 matches -= 1
#             l += 1
#         return matches == 26

                