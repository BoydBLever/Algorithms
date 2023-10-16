# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq, List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap with the first k numbers.
        heap = nums[:k]
        heapq.heapify(heap)
        
        # For each remaining number, if it's larger than the smallest in the heap, replace it.
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        
        # The smallest in the heap is the kth largest in the list.
        return heap[0]