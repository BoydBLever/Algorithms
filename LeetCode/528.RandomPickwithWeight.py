class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        self.n = len(w)
        self.prob = [w[i] / self.total for i in range(self.n)]
        for i in range(1, self.n):
            self.prob[i] += self.prob[i - 1]

    def pickIndex(self) -> int:
        rand = random.random()
        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if rand <= self.prob[mid]:
                r = mid
            else:
                l = mid + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()