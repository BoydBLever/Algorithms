class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(n + 1):
            count = 0
            number = i
            while number > 0:
                if number & 1:
                    count += 1
                number >>= 1
            result[i] = count
        
        return result