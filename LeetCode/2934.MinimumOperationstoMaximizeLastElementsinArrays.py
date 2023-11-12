# Credits to vincent_great
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def check(a, b):
            count, mx1, mx2 = 0, 0, 0
            for x, y in zip(nums1[:-1], nums2[:-1]):
                if a >= max(mx1, x) and b>=max(mx2, y):
                    mx1, mx2 = max(mx1, x), max(mx2, y)
                elif a >= max(mx1, y) and b>=max(mx2, x):
                    mx1, mx2 = max(mx1, y), max(mx2, x)
                    count += 1
                else:
                    return len(nums1)+10
            return count
        ans = min(check(nums1[-1], nums2[-1]), check(nums2[-1], nums1[-1])+1)
        return ans if ans<len(nums1) else -1