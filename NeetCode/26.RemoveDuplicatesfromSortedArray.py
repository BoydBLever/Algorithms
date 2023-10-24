# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# NeetCode solution
from typing import List

# Define a new class called Solution.
class Solution:
    # Define a method within the class called removeDuplicates.
    # This method takes in a list of integers (nums) and returns an integer.
    def removeDuplicates(self, nums: List[int]) -> int:
        # Set the left pointer l to 1.
        # This is the position where the next unique element will be placed.
        l = 1

        # Iterate through the list nums using a right pointer r, starting from index 1.
        for r in range(1, len(nums)):
            # If the current number (at r) is not equal to the previous number (at r-1).
            # This checks for duplicates.
            if nums[r] != nums[r - 1]:
                # Place the unique number from r at the position pointed by l.
                nums[l] = nums[r]
                # Increment the left pointer. This updates the next position where the unique element will be placed.
                l += 1
        # Once the loop completes, l will be the length of the list without duplicates. Return l.
        return l

# The list nums is sorted. So, the idea behind starting with l=1 and r=1 is to compare each number with its preceding one (i.e., nums[r] with nums[r-1]). The first element (nums[0]) doesn't need to be checked because there's no preceding element to compare with.

# Once r starts moving, we compare the element at r with the one before it (r-1). If they are different, it means nums[r] is a unique element (considering the sorted nature of the list), and we place it at the position l and then increment l. The next unique element found will be placed at the next position of l, and so on.

# By the end of this process, all unique elements will have been moved to the start of the list, and the position of l will be the length of the list without duplicates.