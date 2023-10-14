# https://leetcode.com/problems/backspace-string-compare/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = len(s) - 1
        j = len(t) - 1
        s_skip = t_skip = 0
        
        while i >= 0 or j >= 0:
            while i >= 0 and (s[i] == '#' or s_skip > 0):
                if s[i] == '#':
                    s_skip += 1
                else:
                    s_skip -= 1
                i -= 1
                
            while j >= 0 and (t[j] == '#' or t_skip > 0):
                if t[j] == '#':
                    t_skip += 1
                else:
                    t_skip -= 1
                j -= 1
                
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i >= 0) != (j >= 0):
                return False
            
            i -= 1
            j -= 1
        
        return True

