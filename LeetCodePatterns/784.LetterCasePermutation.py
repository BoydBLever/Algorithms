class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtrack(current, s, index, result):

            if index == len(s):
                result.append(current)
                return
            
            if s[index].isalpha():
                backtrack(current + s[index].lower(), s, index + 1, result)
                backtrack(current + s[index].upper(), s, index + 1, result)
            else:
                backtrack(current + s[index], s, index + 1, result)

        backtrack("", s, 0, result)
        return result