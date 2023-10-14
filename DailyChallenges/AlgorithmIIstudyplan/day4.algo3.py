# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        j = n - 1
        max_area = 0
        
        while i < j:
            h_i = height[i]
            h_j = height[j]
            width = j - i
            area = min(h_i, h_j) * width
            max_area = max(max_area, area)
            
            if h_i < h_j:
                i += 1
            else:
                j -= 1
        
        return max_area
# To solve this problem, we can use the two-pointer approach. We start with two pointers, one at the beginning and one at the end of the array. We compute the area of the container between the two pointers and update the maximum area seen so far. Then we move the pointer that points to the shorter line inward, since moving the pointer that points to the taller line inward will only decrease the area. We continue this process until the two pointers meet.
# We use two pointers i and j to point to the left and right ends of the array, respectively. We also initialize a variable max_area to store the maximum area seen so far. We use a while loop to iterate over the array. Inside the loop, we compute the area of the container between the two pointers using the formula area = min(height[i], height[j]) * (j - i). We update the maximum area seen so far if the computed area is greater than the current maximum. Then we move the pointer that points to the shorter line inward, since moving the pointer that points to the taller line inward will only decrease the area. Once the two pointers meet, we return the maximum area seen so far.
# The time complexity of this solution is O(n), where n is the length of the array, since we only iterate over the array once. The space complexity is O(1), since we only use a constant amount of additional space to store some variables.