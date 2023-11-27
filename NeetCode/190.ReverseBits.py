class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):  # Since n is a 32-bit number
            reverse <<= 1  # Shift reverse to the left to make room for the next bit
            reverse |= (n & 1)  # Add the least significant bit of n to reverse
            n >>= 1  # Shift n to the right to process the next bit
        return reverse