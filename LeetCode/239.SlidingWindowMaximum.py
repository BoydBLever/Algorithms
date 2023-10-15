# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize the result list and a deque
        result = []
        deq = deque()

        # Iterate through each element in nums
        for i in range(len(nums)):
            # Remove indices that are out of bound for the current window
            while deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove indices whose corresponding values are less than current element
            # as they are not useful anymore
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()

            # Add the current element's index
            deq.append(i)

            # Add to result the front of the deque (maximum for current window)
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result
    
    #Neetcode Solution
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     output = []
    #     q = collections.deque()
    #     l = r = 0

    #     while r < len(nums):
    #         while q and nums[q[-1]] < nums[r]:
    #         q.pop()
    #         q.append(r)

    #         #remove left val from window
    #         if l > q[0]:
    #             q.popleft()

    #         if (r + 1) >= k:
    #             output.append(nums[q[0]])
    #             l += 1
    #         r += 1
        
    #     return output