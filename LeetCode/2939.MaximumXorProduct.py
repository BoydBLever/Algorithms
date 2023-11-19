# Credits to udhav
class Solution(object):
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = (10 ** 9) + 7

        for index in range(n - 1, -1, -1): # msb -> lsb
            mask = (1 << index)
            a_bit, b_bit = (a & mask), (b & mask)

            # if both bits are 1, then keep them as is
            if a_bit and b_bit:
                continue
            # if both bits are 0, then make them 1 for max product
            elif not a_bit and not b_bit:
                a |= mask
                b |= mask
            else: # one num has 1 while other num has 0
            # as we want both nums to be close to each other, reduce big num by xor mask and increase small num by or mask
                if a_bit and a > b:
                    a ^= mask
                    b |= mask
                elif b_bit and b > a:
                    a |= mask
                    b ^= mask

        a %= mod
        b %= mod
        return (a * b) % mod