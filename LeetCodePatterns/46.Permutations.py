class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            # Base case: a complete permutation is formed
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num not in path:  # Check if the num is already in the current path
                    backtrack(path + [num])

        backtrack([])
        return res