from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)