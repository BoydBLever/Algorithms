# Credits to Ayanerru
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vow = [0] * (n+1)
        vchar = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(1, n+1):
            vow[i] = vow[i-1]
            if s[i-1] in vchar:
                vow[i] += 1

        # we only need to see either vow or con since they're symmetric
        # e.g [0, 2)
        # (v[j] - v[i]) * 2 == (j - i) 
        # v[j] * 2 - j == v[i] * 2 - i
        cond1 = collections.defaultdict(list)
        for i in range(len(vow)):
            cond1[vow[i] * 2 - i].append(i)        
        
        # For a divisor (x*x) % k == 0, find a divisor k2 where x % k2 == 0
        def get_sqrt_divisor(x):
            facs = collections.Counter()
            i = 2
            while i*i <= x:
                while x % i == 0:
                    facs[i] += 1
                    x //= i
                i += 1
            if x > 1:
                facs[x] += 1
            
            res = 1
            for fac, freq in facs.items():
                res *= fac ** ((freq+1) // 2)
            return res
        
        k2 = get_sqrt_divisor(k)
        
        # condition 2
        # ((j-i) // 2) % k2 == 0
        # (j-i) % (k2 *2) == 0
        ans = 0
        for _, indices in cond1.items():
            k3 = k2 * 2
            cnt2 = collections.Counter()
            for idx in indices:
                ans += cnt2[idx % k3]
                cnt2[idx % k3] += 1
        
        return ans