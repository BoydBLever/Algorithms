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
        return res

# Another solution

maxLength = 1
increasing = 1
decreasing = 1

for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        increasing = decreasing + 1
        decreasing = 1
    elif arr[i] < arr[i - 1]:
        decreasing = increasing + 1
        increasing = 1
    else:
        increasing = 1
        decreasing = 1

    maxLength = max(maxLength, max(increasing, decreasing))
return maxLength