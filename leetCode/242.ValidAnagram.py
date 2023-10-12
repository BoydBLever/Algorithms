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
#Hashmap-based solution
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # 1. If lengths of s and t are different, return False.
#         if len(s) != len(t):
#             return False
        
#         # 2. Create an empty dictionary called char_freq.
#         char_freq = {}
        
#         # 3. For each character in s, increment its frequency in char_freq.
#         for char in s:
#             char_freq[char] = char_freq.get(char, 0) + 1
        
#         # 4. For each character in t:
#         for char in t:
#             # If character not in char_freq or its frequency is zero, return False.
#             if char_freq.get(char, 0) == 0:
#                 return False
#             # Decrement its frequency in char_freq.
#             char_freq[char] -= 1
        
#         # 5. Return True.
#         return True

# # Redefining the test cases for the anagram problem
# test_cases_anagram = [
#     ("anagram", "nagaram", True),
#     ("rat", "car", False)
# ]

# # Testing the hashmap-based solution
# test_results_hashmap = [(test[0], test[1], solution.isAnagram(test[0], test[1]), test[2]) for test in test_cases_anagram]
# test_results_hashmap

# NeetCode solution using hashmap
# class Solution:
#     def isAnagram(self, s:str, t:str) -> bool:
#     if len(s) != len(t):
#         return False
    
#     countS, countT = {}, {}

#     for i in range(len(s)):
#         countS[s[i]] = 1 + countS.get(s[i], 0)
#         countT[t[i]] = 1 + countT.get(t[i], 0)
#     for c in countS:
#         if countS[c] != countT.get(c, 0):
#             return False
    
#     return True