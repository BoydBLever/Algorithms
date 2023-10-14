# https://leetcode.com/problems/minimize-deviation-in-array/post-solution/?submissionId=904271090
# Intuition
# The problem requires us to perform two operations on any element of the array any number of times. We can either divide an even number by 2 or multiply an odd number by 2. To find the minimum deviation, we need to transform the array such that the maximum difference between any two elements in the array is minimized. This suggests that we should try to make the elements in the array as close to each other as possible.

# Approach
# We can start by iterating through the array and modifying the odd elements to be even by multiplying them by 2, and keeping track of the minimum value in the array after modifications. We can use a priority queue (min heap) to keep track of the modified elements. We can then find the maximum value in the priority queue and calculate the initial deviation by subtracting the minimum value from the maximum value.

# We can then repeatedly perform the operation that gives the largest increase in deviation until the deviation cannot be increased further. We can do this by popping the smallest element from the priority queue, dividing it by 2, and inserting it back into the priority queue. We update the minimum value as we go, which keeps track of the minimum value in the array after modifications, and the minimum deviation we have seen so far.

# We keep doing this until the top element in the priority queue becomes odd, at which point we cannot increase the deviation any further.

# Complexity
# - Time complexity:
# The time complexity of this algorithm is O(n log n), where n is the length of the input array. This is because we need to iterate through the array once to perform the initial modifications, and then we need to perform n/2 operations to halve the largest element in the priority queue. Each operation takes O(log n) time, which is the time complexity of adding or removing an element from a priority queue.

# - Space complexity:
# The space complexity of this algorithm is O(n), where n is the length of the input array. This is because we need to store the modified elements in a priority queue, which can have up to n elements in the worst case. We also need to keep track of the minimum value in the array after modifications, which requires O(1) space.

# Code
import heapq

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pq = []
        minVal = float('inf')
        for num in nums:
            if num % 2 == 1:
                heapq.heappush(pq, -num * 2)
                minVal = min(minVal, num * 2)
            else:
                heapq.heappush(pq, -num)
                minVal = min(minVal, num)
        minDev = -pq[0] - minVal
        while pq[0] % 2 == 0:
            val = -heapq.heappop(pq)
            if val // 2 >= minVal:
                heapq.heappush(pq, -val // 2)
            else:
                heapq.heappush(pq, -minVal)
            minVal = min(minVal, val // 2)
            minDev = min(minDev, -pq[0] - minVal)
        return minDev