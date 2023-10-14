# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        if not t or not s:
            return ""

        # Dictionary to keep a count of all the unique characters in t.
        t_count = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(t_count)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in t_count and window_counts[character] == t_count[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `l` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in t_count and window_counts[character] < t_count[character]:
                    formed -= 1

                # Move the left pointer ahead
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
#Neetcode solution
# def minWindow(self, s: str, t: str) -> str:
#     if t == "": return ""

#     countT, window = {}, {}

#     for c in t:
#         countT[c] = 1 + countT.get(c, 0)

#     have, need = 0, len(countT)
#     res, resLen = [-1, -1], float("infinity")
#     l = 0
#     for r in range(len(s)):
#         c = s[r]
#         window[c] = 1 + window.get(c, 0)

#         if c in countT and window[c] == countT[c]
#             have += 1
        
#         while have == need:
#             # update our result
#             if (r - 1 + 1) < resLen:
#                 res = [l, r]
#                 resLen = (r - l + 1)
#             #pop from the Left of our window
#             window[s[l]] -= 1
#             if s[l] in countT and window[s[l]] < countT[s[l]]
#                 have -= 1
#             l += 1

#         l, r = res
#         return s[l:r+1] if resLen != float("infinity") else ""
