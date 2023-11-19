# Credits to prathamesh-003
class Solution:
    def minimumSteps(self, s):
        cnt = 0
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                ans += cnt
            else:
                cnt += 1
        return ans