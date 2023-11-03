class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize the hash set
        seen = set()
        # Iterate over each number in the list
        for n in nums:
            # If number is already in the set, we found a duplicate.
            if n in seen:
                return True
            # Otherwise, add the number to the set
            else:
                seen.add(n)
        # If we reach here, no duplicates were found
        return False
    # Time Complexity: O(n)
    # Space Complexity: O(n)