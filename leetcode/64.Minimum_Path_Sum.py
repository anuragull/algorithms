"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        N = len(grid)
        if N == 0:
            return 0
        M = len(grid[0])
        
        dp = [[0 for i in range(M)] for i in range(N)]
        
        dp[0][0] = grid[0][0]
        # init the first part
        for i in range(1, M):
            dp[0][i] = grid[0][i] + dp[0][i-1]
            
        for i in range(1, N):
            dp[i][0] = grid[i][0] + dp[i-1][0]
            
        for i in range(1, N):
            for j in range(1, M):
                if i ==0  or j == 0:
                    continue
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[N-1][M-1]
    
