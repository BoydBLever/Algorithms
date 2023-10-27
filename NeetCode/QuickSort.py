from typing import List
# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return

        pivot = pairs[e]  # Right most
        left = s

        for i in range(s, e):
            # Partition
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, s, left - 1)  # left
        self.quickSortHelper(pairs, left + 1, e)  # right


# Time Complexity: O(nlogn) Space Complexity: O(n)
# Test processing function
def test():
    solution = Solution()
    raw_pairs = [(1, "x"), (2, "y"), (3, "z"), (2, "a"), (1, "b"), (3, "c")]
    pairs = [Pair(key, value) for key, value in raw_pairs]
    sorted_pairs = solution.quickSort(pairs)
    for pair in sorted_pairs:
        print(pair.key, pair.value)
if __name__ == '__main__':
    test()