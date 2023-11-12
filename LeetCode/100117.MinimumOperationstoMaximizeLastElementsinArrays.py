class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # Get the maximum values initially
        max_num1, max_num2 = max(nums1[:-1]), max(nums2[:-1])
        # Initialize the number of operations
        operations = 0
        
        while nums1[-1] < max_num1 or nums2[-1] < max_num2:
            # Find the index of the minimum increment needed for nums1 and maximum decrement for nums2
            diff_num1 = [x - nums1[-1] for x in nums1[:-1]]
            diff_num2 = [nums2[-1] - x for x in nums2[:-1]]
            
            # If no more operations can increase nums1's last element or decrease nums2's last element
            if not diff_num1 and not diff_num2:
                return -1
            
            # Select the swap that gives the maximum benefit
            if diff_num1 and diff_num2:
                max_diff1_idx = diff_num1.index(max(diff_num1))
                max_diff2_idx = diff_num2.index(max(diff_num2))
                
                if diff_num1[max_diff1_idx] > diff_num2[max_diff2_idx]:
                    nums1[-1], nums1[max_diff1_idx] = nums1[max_diff1_idx], nums1[-1]
                else:
                    nums2[-1], nums2[max_diff2_idx] = nums2[max_diff2_idx], nums2[-1]
            elif diff_num1:
                max_diff1_idx = diff_num1.index(max(diff_num1))
                nums1[-1], nums1[max_diff1_idx] = nums1[max_diff1_idx], nums1[-1]
            else:
                max_diff2_idx = diff_num2.index(max(diff_num2))
                nums2[-1], nums2[max_diff2_idx] = nums2[max_diff2_idx], nums2[-1]

            # Update the maximum values and operation count
            max_num1, max_num2 = max(nums1[:-1]), max(nums2[:-1])
            operations += 1

            # If we have achieved the goal, break out of the loop
            if nums1[-1] >= max_num1 and nums2[-1] >= max_num2:
                break

        return operations