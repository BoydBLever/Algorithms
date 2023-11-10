class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Edge Case
        if not nums:
            return -1
        # Binary Search: works by repeatedly dividng the search space in half.
        # Use two pointers to track the left and right bound. Left and right bound are the index of the array. Left is the first element and right is the last element.
        left, right = 0, len(nums)-1
        # Use while loop to iterate over the array
        # While left is less than or equal to right, we will continue to iterate over the array
        while left <= right:
            # Find the index of the middle element. The mid index is the average of the left and right bound.
            mid = (left + right) // 2
            # If the middle element is equal to the target, return the index of the middle element
            if nums[mid] == target:
                return mid
            # nums[left] is the value of the first element, nums[mid] is the value of the middle element, nums[right] is the value of the last element
            if nums[left] <= nums[mid]:
                # if the target is between the first element and the middle element, we will update the right bound to mid - 1
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # if the target is not between the first element and the middle element, we will update the left bound to mid + 1
                else:
                    left = mid + 1
            # else if the target is between the middle element and the last element, we will update the left bound to mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
            # else if the target is not between the middle element and the last element, we will update the right bound to mid - 1
                else:
                    right = mid - 1
        return -1
    # Time: O(logN)
    # Space: O(1)