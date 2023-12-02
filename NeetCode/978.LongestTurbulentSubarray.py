class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
          # 9,> 4,> 2,< 10, >7, <8,= 8, >1, <9
          # return length of the subarray with longest streak of alternating equality signs i.e. return 5
        l, r = 0, 1
        res, prev = 1, ""
        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r -1 + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""