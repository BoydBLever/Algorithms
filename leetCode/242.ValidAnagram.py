#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. If lengths of s and t are different, return False.
        if len(s) != len(t):
            return False
        
        # 2. Initialize a list of zeros of size 26 (for 26 English letters).
        counter = [0] * 26
        
        # 3. For each character in s, increment its corresponding index in the frequency counter.
        for char in s:
            counter[ord(char) - ord('a')] += 1
        
        # 4. For each character in t, decrement its corresponding index in the frequency counter.
        for char in t:
            counter[ord(char) - ord('a')] -= 1
        
        # 5. If all elements in the frequency counter are zero, return True. Else, return False.
        return all(val == 0 for val in counter)

# Testing the function again
solution = Solution()
solution.isAnagram("anagram", "nagaram")
