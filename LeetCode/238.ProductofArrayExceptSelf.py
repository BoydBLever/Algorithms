# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize left and right product lists with ones
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        
        # 3. Initialize a left_running_product variable to 1.
        left_running_product = 1
        
        # 4. For each number from left to right:
        for i in range(1, len(nums)):
            left_running_product *= nums[i - 1]
            left_products[i] = left_running_product
        
        # 5. Initialize a right_running_product variable to 1.
        right_running_product = 1
        
        # 6. For each number from right to left:
        for i in range(len(nums) - 2, -1, -1):
            right_running_product *= nums[i + 1]
            right_products[i] = right_running_product
        
        # 8. For each index, multiply the left_product by the right_product for that index
        result = [left_products[i] * right_products[i] for i in range(len(nums))]
        
        # 9. Return the result list.
        return result

# Example test case
solution = Solution()
test_input = [1, 2, 3, 4]
solution.productExceptSelf(test_input)