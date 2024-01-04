class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums) # count[n] = c
        res = 0
        for n, c in count.items():
            if c == 1:
                return -1
            res += math.ceil(c / 3)
        return res
# Time complexity: O(N)
# Space complexity: O(N)
