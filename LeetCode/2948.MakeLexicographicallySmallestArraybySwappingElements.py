# Credits to MarkSPhilip31
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        a = [(nums[i], i) for i in range(len(nums))]
        a.sort(key=lambda x: x[0])
        
        x, y = [[] for _ in range(len(nums))], [[] for _ in range(len(nums))]
        
        j, cur = 0, a[0][0]
        x[j].append(a[0][0])
        y[j].append(a[0][1])
        for i in range(1, len(nums)):
            if a[i][0] - cur > limit:
                j += 1
            x[j].append(a[i][0])
            y[j].append(a[i][1])
            cur = a[i][0]
        
        for i in range(len(nums)):
            y[i].sort()
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(x[i])):
                res[y[i][j]] = x[i][j]
        
        return res
