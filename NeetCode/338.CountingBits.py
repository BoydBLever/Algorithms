# https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, n: int) -> List[int]:
        # why (n + 1)? because we need to include 0
        result = [0] * (n + 1)
        # why range(n + 1)? because we need to include n
        for i in range(n + 1):
            count = 0
            number = i
            while number > 0:
                if number & 1:
                    count += 1
                number >>= 1
            result[i] = count
        
        return result