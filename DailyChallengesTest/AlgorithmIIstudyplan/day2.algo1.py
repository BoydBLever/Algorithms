# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
# One efficient solution to this problem is to use binary search to find the minimum element. The idea is to find the pivot point, which is the index of the smallest element in the array. Once we find the pivot, the minimum element will be the element at the pivot index.

# To find the pivot point, we can modify the binary search algorithm. We can compare the middle element with the last element of the array. If the middle element is greater than the last element, then the pivot must be in the second half of the array. Otherwise, the pivot must be in the first half of the array. We keep dividing the array into halves until we find the pivot.