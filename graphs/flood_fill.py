def flood_fill():
  """
  https://leetcode.com/problems/flood-fill/
  
  Solution :
  1. find old_color at sr, sc
  2. start DFS at sr,sc and then recursively in four direction if the [i][j] == old_color
  
  """
    m = len(image)
    n = len(image[0]) if image else 0
    old_color = image[sr][sc]
    if old_color == color: return image

    def dfs(r,c):
        if image[r][c] == old_color:
            image[r][c] = color
            if r >= 1 : dfs(r-1, c)
            if r+ 1 < m : dfs(r+1, c)
            if c >= 1 : dfs(r, c-1)
            if c+1 < n : dfs(r, c+1)
    dfs(sr, sc)
    return image
