class Solution:
    def missingNumber(self, nums: [int]) -> int:
        # Create a hash set
        seen = set()

        # n is the length of nums
        n = len(nums)

        # Populate the hash set with numbers 0 to n
        for number in range(0, n + 1):
            seen.add(number)
        
        # For each number in nums, remove that number from the set
        for number in nums:
            seen.discard(number)  # Using discard() instead of remove() to avoid KeyError if element not found
        
        # The remaining number in seen is the missing number
        # As there's only one number left, you can return it directly
        return seen.pop()
    # Time complexity: O(n)
    # Space complexity: O(n)
    
    # Solution 2: using bitwise operator XOR (^)
    # class Solution:
    # def missingNumber(self, nums: [int]) -> int:
    #     missing = len(nums)
    #     for i, num in enumerate(nums):
    #         missing ^= i ^ num
    #     return missing
    # Time complexity: O(n)
    # Space complexity: O(1)
