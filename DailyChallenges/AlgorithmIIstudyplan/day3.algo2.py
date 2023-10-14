# https://leetcode.com/problems/3sum/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to avoid duplicate triplets
        nums.sort()
        n = len(nums)
        result = []
        
        # Fix the first element of the triplet
        for i in range(n-2):
            # Skip over duplicate elements
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Use two pointers to find the remaining two elements
            left = i + 1
            right = n - 1
            
            while left < right:
                # Calculate the sum of the three elements
                triplet_sum = nums[i] + nums[left] + nums[right]
                
                if triplet_sum < 0:
                    # Move the left pointer to the right
                    left += 1
                elif triplet_sum > 0:
                    # Move the right pointer to the left
                    right -= 1
                else:
                    # Add the triplet to the result and move the left pointer to the right to avoid duplicate triplets
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        
        return result
    
# One approach to solve this problem is to use a nested loop to fix the first element of the triplet, and use two pointers to find the remaining two elements. We sort the array to avoid duplicate triplets. For each element in the array, we use two pointers - one starting from the element next to it, and the other starting from the end of the array. We calculate the sum of the three elements, and move the pointers accordingly. If the sum is less than zero, we move the left pointer to the right. If the sum is greater than zero, we move the right pointer to the left. If the sum is zero, we add the triplet to the result and move the left pointer to the right to avoid duplicate triplets.