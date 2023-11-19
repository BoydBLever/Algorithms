class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        num_set = set()
        
        for num in nums:
            if num in num_set:
                duplicates.append(num)
            else:
                num_set.add(num)
        
        return duplicates
# Time complexity: O(n)
# Space complexity: O(n)