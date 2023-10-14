# * @param {string} s
# * @param {string[]} wordDict
# * @return {string[]}
# *
# * Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word.
# * Return all such possible sentences in any order.
# *
# * Note that the same word in the dictionary may be reused multiple times in the segmentation.
# *
# * https://leetcode.com/problems/word-break-ii/

string1 = "catsanddog"
word1 = ["cat", "cats", "and", "sand", "dog"]
expect1 = ["cats and dog", "cat sand dog"]

string2 = "pineapplepenapple"
word2 = ["apple", "pen", "applepen", "pine", "pineapple"]
expect2 = ["pine apple pen apple",
           "pineapple pen apple", "pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

string3 = "catsandog"
word3 = ["cats", "dog", "sand", "and", "cat"]
expect3 = []

class Solution(object):
    def wordBreak(self, s, wordDict):
        def backtrack(s, wordDict, start, path, res):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict:
                    path.append(s[start:end])
                    backtrack(s, wordDict, end, path, res)
                    path.pop()
                    
        res = []
        backtrack(s, set(wordDict), 0, [], res)
        return [" ".join(x) for x in res]


# def wordBreakLVL2(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """

print(wordBreakLVL2(string1, word1))
print(wordBreakLVL2(string2, word2))
print(wordBreakLVL2(string3, word3))
# Explanation:
# The wordBreak function takes two inputs: a string s and a dictionary of strings wordDict. The goal is to add spaces in s to construct a sentence where each word is a valid dictionary word, and return all such possible sentences.

# The solution uses a backtracking approach to find all possible combinations of words that can be formed from the given string s. The main idea behind the backtracking approach is to try different combinations of words and keep track of the current combination using a path list. If the current combination is a valid sentence, it is added to the result res. If the current combination is not a valid sentence, we "backtrack" by removing the last added word and trying a different combination.

# The backtracking is done using the backtrack helper function, which takes the following inputs:

# s: the input string
# wordDict: the dictionary of words
# start: the current starting index in the string s
# path: the current combination of words
# res: the result list
# The backtrack function starts by checking if the current start index is equal to the length of the string s. If it is, it means that all the characters in the string have been processed and a valid sentence has been formed, so it adds the current path to the result res.

# If the current start index is not equal to the length of the string s, the function loops through all possible end indices, starting from start + 1 and ending at the length of the string s + 1. For each end index, it checks if the substring from start to end is in the dictionary. If it is, the function adds the substring to the path, and then calls itself recursively with the updated start index equal to end. This continues the process of trying different combinations of words.

# Once the recursive call returns, the function removes the last added word from the path, effectively "backtracking" to try a different combination.

# Finally, the main wordBreak function converts the result res list of lists of words into a list of sentences, where each sentence is a string formed by joining the words in each list with a space.

# The backtrack function takes the following parameters:

# s: the input string s
# wordDict: a set of valid words that can be used to form sentences
# start: the starting index in the string s from which to find the next word
# path: a list that represents the current combination of words that have been found so far
# res: a list of lists, where each list represents a valid sentence formed from the words in wordDict
# The start parameter is used to keep track of the current starting index in the string s as the function iterates through different combinations of words. The path parameter is used to store the current combination of words, and the res parameter is used to store the final result of all valid sentences that can be formed from the string s and the words in wordDict.

# The backtrack function starts by checking if the current start index is equal to the length of the string s. If it is, it means that all the characters in the string have been processed and a valid sentence has been formed, so it adds the current path to the result res.

# If the current start index is not equal to the length of the string s, the function loops through all possible end indices, starting from start + 1 and ending at the length of the string s + 1. For each end index, it checks if the substring from start to end is in the dictionary. If it is, the function adds the substring to the path, and then calls itself recursively with the updated start index equal to end. This continues the process of trying different combinations of words.

# Once the recursive call returns, the function removes the last added word from the path, effectively "backtracking" to try a different combination.

# This solution does not use backtracking. It uses dynammic programming.

class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                    
        def construct(s, wordDict, end, dp, path, res):
            if end == 0:
                res.append(" ".join(path[::-1]))
                return
            
            for j in range(end):
                if dp[j] and s[j:end] in wordDict:
                    path.append(s[j:end])
                    construct(s, wordDict, j, dp, path, res)
                    path.pop()
                    
        res = []
        construct(s, wordDict, n, dp, [], res)
        return res

# This dynamic programming solution has a time complexity of O(n^2), which is much better than the exponential time complexity of the backtracking solution. However, it requires additional memory to store the dp array, which may not be ideal for some problems with limited memory constraints.

# In general, the dynamic programming solution to the wordBreak problem is faster than the backtracking solution. The time complexity of the dynamic programming solution is O(n^2), where n is the length of the input string s. This is much better than the exponential time complexity of the backtracking solution, which is O(2^n) in the worst case.

# Additionally, the dynamic programming solution requires less memory than the backtracking solution, as it does not need to maintain a recursive call stack. Instead, it uses a single array dp to store intermediate results.

# So, in terms of efficiency and scalability, the dynamic programming solution beats the backtracking solution for the wordBreak problem. However, the backtracking solution is generally easier to understand and implement, especially for those who are not familiar with dynamic programming.

# In the end, the choice between the two solutions depends on the specific requirements of the problem and the trade-offs between time and space complexity, ease of implementation, and other factors.
