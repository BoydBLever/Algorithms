class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Find the range of numbers
        low = 1
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            # Count the numbers in the range [low, mid]
            for num in nums:
                if num <= mid:
                    count += 1
            
            # If the count is greater than the range size, the duplicate is in the range [low, mid]
            if count > mid - low + 1:
                high = mid
            else:
                low = mid + 1
        
        # Step 2: Find the duplicate number using two pointers
        slow = fast = low
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # Step 3: Return the duplicate number
        return slow
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)

# Set Solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)