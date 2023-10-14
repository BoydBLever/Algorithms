class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


# This code is very similar to the JavaScript code that we saw earlier. We start by initializing a variable shift to 0, and then we keep shifting both left and right to the right by 1 until left is no longer less than right. For each shift, we increment shift by 1.

# fter the loop, we shift left to the left by shift bits, and return the result. This gives us the bitwise AND of all the numbers in the range.

# To use this code, you can create an instance of the Solution class and call the rangeBitwiseAnd method with the left and right values as parameters. For example:

# s = Solution()
# result = s.rangeBitwiseAnd(5, 7)
# print(result)  # Output: 4

# This will output the bitwise AND of all numbers in the range [5, 7], which is 4.