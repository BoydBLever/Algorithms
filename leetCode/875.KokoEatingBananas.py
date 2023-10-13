# https://leetcode.com/problems/koko-eating-bananas/
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to determine if Koko can eat all bananas at the given speed
        def canEatAll(speed: int) -> bool:
            # Calculate the total hours needed to eat all bananas at the given speed
            hours_needed = sum((pile + speed - 1) // speed for pile in piles)
            # Return True if Koko can eat all bananas within 'h' hours at the given speed
            return hours_needed <= h
        
        # Initialize the search range for Koko's eating speed: 1 to the maximum number of bananas in a pile
        low, high = 1, max(piles)
        
        # Binary search to find the minimum eating speed
        while low < high:
            mid = (low + high) // 2
            if canEatAll(mid):
                high = mid
            else:
                low = mid + 1
        
        return low

# Testing the function on given examples
results_11 = [(test[0], Solution().minEatingSpeed(*test[0]) == test[1]) for test in test_cases_11]
results_11
#Neetcode solution
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         l, r = 1, max(piles)
#         res = r

#         while l <= r:
#             k = (l + r) // 2
#             hours = 0
#             for p in piles:
#                 hours += math.ceil(p / k)

#             if hours <= h:
#                 res = min(res,k)
#                 r = k - 1
#             else:
#                 l = k + 1
#         return res
            