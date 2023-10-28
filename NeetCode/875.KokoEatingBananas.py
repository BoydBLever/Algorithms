# The optimal solution for this problem is to use binary search.
# Leetcode: 875. Koko Eating Bananas
# NeetCode solution 
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Binary search
        # Time: O(NlogW), where N is the number of piles, and W is the maximum size of a pile.
        # Space: O(1)
            l, r = 1, max(piles)
            res = r
            
            while l <= r:
                k = (l + r) // 2
                hours = 0
                for p in piles:
                    hours += math.ceil(p / k)
                if hours <= h:
                    res = min(res, k)
                    r = k - 1
                else:
                    l = k + 1
            
            return res