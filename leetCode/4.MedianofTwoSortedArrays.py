# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array; if not, swap nums1 and nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Set x and y to the lengths of nums1 and nums2, respectively
        x, y = len(nums1), len(nums2)
        
        # Initialize two pointers: low and high for binary search on the smaller array
        low, high = 0, x
        
        # Start binary search
        while low <= high:
            # Partition nums1 and nums2 such that the number of elements on the left side and right side are equal
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # If partitionX is 0, it means there is no element on the left side of nums1, so set maxX to negative infinity
            # Otherwise, set maxX to the last element on the left side of nums1
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            
            # Similarly for minX
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            # Same logic applied for nums2
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we found the correct partition
            if maxX <= minY and maxY <= minX:
                # If the total number of elements is even, return the average of max of left elements and min of right elements
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                # Otherwise, return max of left elements
                else:
                    return max(maxX, maxY)
            # If maxX > minY, move towards the left side of nums1
            elif maxX > minY:
                high = partitionX - 1
            # If maxY > minX, move towards the right side of nums1
            else:
                low = partitionX + 1

        # If no partition is found, it means the arrays are not sorted, which is not possible according to the problem statement
        raise ValueError("Input arrays are not sorted.")

# Testing the function on a couple of examples
results_15 = [(test[:-1], Solution().findMedianSortedArrays(*test[:-1]) == test[-1]) for test in test_cases_15]
results_15

#Neetcode solution
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         A, B = nums1, nums2
#         total = len(nums1) + len(nums2)
#         half = total // 2

#         if len(B) < len(A)
#             A, B = B, A
        
#         l, r = 0, len(A) - 1
#         while True:
#             i = (l + r) // 2 #A
#             j = half - i - 2 #B

#             Aleft = A[i] if i >= 0 else float("-infinity")
#             Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
#             Bleft = B[j] if j >= 0 else float("-infinity")
#             Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

#             # partition is correct
#             if Aleft <= Bright and Bleft <= Aright:
#                 #odd
#                 if total % 2:
#                     return min(Aright, Bright)
#                 #even
#                 return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
#             elif Aleft > Bright:
#                 r = i - 1
#             else:
#                 l = i + 1