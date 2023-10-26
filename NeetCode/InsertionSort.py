# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
from typing import List

class Pair:
    ...

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        res = [pairs.copy()]
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            res.append(pairs.copy())
        return res
# Time: O(N ^ 2) Space: O(N)

# Actual definition of Pair
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

# Test processing function
def test_process():
    pairs = [Pair(5, 'apple'), Pair(2, 'banana'), Pair(9, 'cherry')]
    sol = Solution()
    res = sol.insertionSort(pairs)
    for pair_list in res:
        for p in pair_list:
            print(p.key, p.value)
        print('---')
test_process()