# Credits to NeetCode
from typing import List, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res

# Optimized
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         maxHeap = []
#         for (x, y) in points:
#             dist = -(x ** 2 + y ** 2)  # Negate the distance for max heap
#             if len(maxHeap) < k:
#                 heapq.heappush(maxHeap, (dist, x, y))
#             else:
#                 heapq.heappushpop(maxHeap, (dist, x, y))

#         return [[x, y] for (dist, x, y) in maxHeap]
