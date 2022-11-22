def num_province(isConnected):
    """
    Algo :
    1. Create undirected adj list for all the connected cities 
    2. for each city, if its not visited means a province update the counter, 
    3. DFS with each nieghbor, skip if already visited  
    
    Complexity : O(V + E) 
    """
    
        graph = collections.defaultdict(list)
        
        if not isConnected:
            return 0
        
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visit = [False]*n
        
        def dfs(u):
            for v in graph[u]:
                if visit[v] == False:
                    visit[v] = True
                    dfs(v)
        
        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                dfs(i)
        
        return count
