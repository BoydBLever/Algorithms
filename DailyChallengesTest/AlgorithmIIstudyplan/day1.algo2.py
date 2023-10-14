# https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan&id=algorithm-ii
class Solution:
    def search(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[left]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
# This approach works by splitting the rotated sorted array into two halves and checking which half is sorted. If the left half is sorted, we check if the target is within the range of the left half, and if it is, we continue the binary search in the left half. Otherwise, we continue the binary search in the right half. If the right half is sorted, we check if the target is within the range of the right half, and if it is, we continue the binary search in the right half. Otherwise, we continue the binary search in the left half.