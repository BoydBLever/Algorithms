class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        # The strategy is to set the highest bits of the result of a XOR x and b XOR x.
        # To maximize the product, we want to set the highest bit possible in the result of a XOR x.
        # Since x is less than 2^n, the highest bit we can affect is the n-1 th bit.
        # We should set this bit if it's not already set in a or b.
        # Then, for each bit position from n-1 down to 0, if the bit is not set in a or b, we set it in x.
        # Initialize x to 0
        x = 0
        # Iterate over each bit position
        for i in range(n - 1, -1, -1):
            # Check if the bit is not set in both a and b
            if not (a & (1 << i)) or not (b & (1 << i)):
                # Set this bit in x
                x |= (1 << i)
        
        # Calculate the product
        product = (a ^ x) * (b ^ x)
        
        # Since the answer may be too large, return it modulo 10^9 + 7
        return product % (10**9 + 7)

# Create an instance of the Solution class
sol = Solution()

# Test the method with the provided examples
print(sol.maximumXorProduct(12, 5, 4)) # Expected output: 98
print(sol.maximumXorProduct(6, 7, 5))  # Expected output: 930
print(sol.maximumXorProduct(1, 6, 3))  # Expected output: 12