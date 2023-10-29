# https://leetcode.com/contest/weekly-contest-369/problems/maximum-points-after-collecting-coins-from-all-nodes/

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        graph = [[] for _ in range(len(coins))]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            benefits = []
            total = coins[node]

            for child in graph[node]:
                if child == parent:
                    continue
                child_total, child_benefits = dfs(child, node)
                total += child_total
                benefits.extend(child_benefits)

            if not benefits:
                return total, [coins[node], coins[node] // 2 - total]

            benefits.append(coins[node] // 2 - total)
            benefits.sort(reverse=True)

            for i in range(min(k, len(benefits))):
                total += benefits[i]

            return total, benefits[k:]

        return dfs(0, -1)[0]