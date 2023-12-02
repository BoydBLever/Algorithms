[a, b, c, d]

------ First Loop

for i in range(0, n): # generates up to but not including n. Indices start at 0. The final value generated will be the last element, which is at i = n - 1

For an array [a, b, c, d] with 4 elements, n = 4
The indices are, 0, 1, 2, 3.
for i in range(0, 4) will iterate over 0, 1, 2, 3

------ Second Loop

for i in range(0, n):
    for j in range(i, n):
        i= 0
        [a], [a, b], [a, b, c], [a, b, c, d]
        i sets the starting index of the subarray
        j iterates from the starting index, to the end of the arrray, setting the ending index of the subarray

-------- Third Loop 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = float('-inf')

        n = len(nums)

        for i in range(0, n):
            for j in range(i, n):
                subarray_sum = 0
                for k in range(i, j + 1):
                    subarray_sum += nums[k]
                maxSum = max(maxSum, subarray_sum)

        return maxSum
    
Brute Force: Time complexity: O(n^3)

