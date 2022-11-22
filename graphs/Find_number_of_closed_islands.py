def closed_island(grid):
"""
Problem :https://leetcode.com/problems/number-of-closed-islands/

Solution:

1. First assign all the water on the boundry as not 0 (3)
2. Assign all the water that is contigous as 2 
3. Count each such block 

DFS with a top/right/left/bottom 

"""

if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, val):
            if 0<=i<m and 0<=j<n and grid[i][j]==0:
                grid[i][j] = val
                dfs(i, j+1, val)
                dfs(i+1, j, val)
                dfs(i-1, j, val)
                dfs(i, j-1, val)
        # set the border as 1 
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j, 3)
        # find a closed range             
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 2)
                    res += 1
                 
        return res
