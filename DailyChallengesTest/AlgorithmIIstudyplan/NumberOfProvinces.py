class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        if not isConnected:
            return 0
        
        n = len(isConnected)
        count = 0
        
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0
                    isConnected[j][i] = 0
                    dfs(j)
        
        for i in range(n):
            if isConnected[i][i] == 1:
                dfs(i)
                count += 1
        
        return count
