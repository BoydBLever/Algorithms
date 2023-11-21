class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)
    # Time: O(2^n)
    # Space: O(n)

# Decision Tree for [1,2,2] , i = include e = exclude
#                      []
#              / i              \ e
#            [1]                []
#          /       \         /     \
#        [1,2]     [1]     [2]       []
#        /   \      /\     /\        / \
#    [1,2,2][1,2][1,2][1][2,2][2]   [2][]