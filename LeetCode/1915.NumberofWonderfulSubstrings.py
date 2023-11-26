# https://leetcode.com/problems/number-of-wonderful-substrings/description/
# Credits to Day_Tripper
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        c = Counter(accumulate((1 << (ord(ch) - 97) for ch in word), xor, initial = 0))
        out = 0
        for k in c:
            temp = c[k] - 1
            for mask in range(10):
                if (kk := k ^ (1 << mask)) in c:
                    temp += c[kk]
            out += temp * c[k]
        return out // 2