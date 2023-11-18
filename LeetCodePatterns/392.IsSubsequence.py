class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        s_index = 0
        for character in t:
            if character == s[s_index]:
                s_index += 1
            if s_index == len(s):
                return True
        return False