# https://leetcode.com/contest/weekly-contest-369/problems/minimum-increment-operations-to-make-array-beautiful/
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        #Bucket Sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        res = 0
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res += i - 1
                if len(freq[0]) > 0:
                    freq[0].append(n + 1)
                else:
                    freq[0] = [n + 1]
                if len(freq[0]) == k:
                    return res
        return res