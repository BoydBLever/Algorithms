# https://leetcode.com/problems/interval-list-intersections/description/?envType=study-plan&id=algorithm-ii
# To solve this problem, we can use two pointers to iterate over the two lists and find the intersection of intervals. We start with the first interval in both lists and check if they intersect. If they do, we add the intersection to the result list. Then we move the pointer of the interval that ends earlier to the next interval in its list and repeat the process until one of the lists is exhausted.
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        n = len(firstList)
        m = len(secondList)
        res = []
        
        while i < n and j < m:
            a, b = firstList[i]
            c, d = secondList[j]
            if b < c:
                i += 1
            elif d < a:
                j += 1
            else:
                res.append([max(a, c), min(b, d)])
                if b <= d:
                    i += 1
                else:
                    j += 1
        
        return res
