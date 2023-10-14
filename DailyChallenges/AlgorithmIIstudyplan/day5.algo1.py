# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        window_count = {}
        for i in range(len(s)):
            window_count[s[i]] = window_count.get(s[i], 0) + 1
            if i >= len(p):
                if window_count[s[i-len(p)]] == 1:
                    del window_count[s[i-len(p)]]
                else:
                    window_count[s[i-len(p)]] -= 1
            if window_count == p_count:
                result.append(i-len(p)+1)
        return result

# One possible solution to this problem is to use a sliding window technique. We can start by creating two dictionaries, one for the characters in p and another for the characters in the current window of s. We can iterate through s using a sliding window of length p and check if the two dictionaries are equal. If they are, we add the starting index of the current window to the result array. Otherwise, we move the window one position to the right and update the dictionaries accordingly.

# The time complexity of this solution is O(n), where n is the length of s. We iterate through s once and perform constant time operations at each step. The space complexity is also O(n), since we need to store the characters in p and the characters in the current window of s.