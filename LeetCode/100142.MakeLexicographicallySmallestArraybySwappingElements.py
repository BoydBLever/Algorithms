class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            # Find the minimum element in the allowable range of `limit`
            min_val = min(nums[i:min(n, i + limit + 1)])
            if min_val < nums[i]:
                min_index = nums.index(min_val, i, min(n, i + limit + 1))
                # Swap the elements
                nums[i], nums[min_index] = nums[min_index], nums[i]
                # Decrement the limit by the distance we swapped
                limit -= min_index - i
                # If limit is used up, break out of the loop
                if limit <= 0:
                    break
        return nums