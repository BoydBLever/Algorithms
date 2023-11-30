# Credits to Shiran Afergan
import heapq

class Solution:
    def mincostToHireWorkers(self, quality, expWage, k):
        n = len(expWage)
        
        workers = sorted([(w/q, q) for w, q in zip(expWage, quality)])
        
        min_cost = float('inf')
        sum_heap = 0
        max_heap = []

        for i in range(k):
            sum_heap += workers[i][1]
            heapq.heappush(max_heap, -workers[i][1])
        
        min_cost = workers[k - 1][0] * sum_heap

        for captain in range(k, n):
            captain_ratio = workers[captain][0]
            if -max_heap[0] > workers[captain][1]:
                sum_heap += workers[captain][1] + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -workers[captain][1])
            
            cost = captain_ratio * sum_heap
            min_cost = min(min_cost, cost)

        return min_cost
    
    # Time: O(NlogN)
    # Space: O(N)