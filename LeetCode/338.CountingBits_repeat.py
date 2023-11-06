class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (2 + 1)  # [0, 0, 0]

        for i in range(2 + 1):  # i will be 0, then 1, then 2
            count = 0  # Start count at 0 for each number
            number = i  # Set number to be the current i
            while number > 0:  # While there is a number to check
                if number & 1:  # If the least significant bit is 1
                    count += 1  # Increment count
                number >>= 1  # Shift number right by 1 bit to check the next bit
            result[i] = count  # Set the count for this number in the result

        return result
    # result should be [0, 1, 1]
