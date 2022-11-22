def num_islands(grid):
  """
  1. dfs to find the islands in the range 
     a. dfs for only island pixel, 
     b. check for bound if they are not bounded or not island return 
     c. dfs on all 4 direction 
  key is to set the visited grid index as "#"
  """
  
   """
        use dfs to search
        """
        def dfs(i, j):
            if j < 0 or i < 0 or i >= r or j >= c or grid[i][j] != "1":
                return
            # reset the value
            grid[i][j] = '#'
            dfs( i+1, j)
            dfs( i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        count = 0
        if not grid:
            return count
        
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
