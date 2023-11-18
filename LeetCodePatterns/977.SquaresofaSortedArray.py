class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    # Brute Force
        return sorted([i**2 for i in nums])
    # Brute Force Time complexity: O(nlogn) Space complexity: O(n)
    # Two Pointer
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        insert_pos = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[insert_pos] = nums[left] ** 2
                left += 1
            else:
                res[insert_pos] = nums[right] ** 2
                right -= 1
            insert_pos -= 1

        return res       
    # Two Pointer Time complexity: O(n) Space complexity: O(n)                      