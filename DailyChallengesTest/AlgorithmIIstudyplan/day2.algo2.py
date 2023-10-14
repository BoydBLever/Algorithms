# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        
        return left
# One efficient solution to this problem is to use binary search to find a peak element. The idea is to compare the middle element with its neighbors to determine if it is a peak element. If the middle element is greater than both of its neighbors, then we have found a peak element. Otherwise, we move towards the side that has a neighbor greater than the middle element, since there must be a peak in that direction.

# To implement this idea, we can use a modified binary search algorithm. At each iteration, we check if the middle element is a peak element. If it is not, we move towards the side that has a greater neighbor. We keep dividing the search range in half until we find a peak element.