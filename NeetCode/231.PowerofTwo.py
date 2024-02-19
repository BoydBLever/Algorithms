class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n
# Time complexity: O(logN)
# Space complexity: O(1)
# The above solution is not optimal. We can do better.
return n > 0 and (n & (n - 1)) == 0
# Time complexity: O(1)
# Space complexity: O(1)