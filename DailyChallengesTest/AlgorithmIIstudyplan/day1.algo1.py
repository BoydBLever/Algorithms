# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/906225745/?envType=study-plan&id=algorithm-ii
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize variables for left and right indices
        left, right = 0, len(nums) - 1
        
        # Find leftmost index of target using binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # If mid element is target, check if it is the leftmost occurrence
                if mid == 0 or nums[mid-1] != target:
                    start = mid
                    break
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            # Target not found, return [-1, -1]
            return [-1, -1]
        
        # Find rightmost index of target using binary search
        left, right = start, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # If mid element is target, check if it is the rightmost occurrence
                if mid == len(nums) - 1 or nums[mid+1] != target:
                    end = mid
                    break
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Return [start, end] as the result
        return [start, end]