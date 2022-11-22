"""
https://leetcode.com/problems/min-cost-to-connect-all-points/
[Premium] https://leetcode.com/problems/connecting-cities-with-minimum-cost/
[Premium] https://leetcode.com/problems/optimize-water-distribution-in-a-village

MST - Prims algorithm 
Create a set mstSet that keeps track of vertices already included in MST. 
Assign a key value to all vertices in the input graph. 
Initialize all key values as INFINITE. Assign the key value as 0 for the first vertex so that it is picked first. 
While mstSet doesn’t include all vertices 
Pick a vertex u which is not there in mstSet and has a minimum key value. 
Include u in the mstSet. 
Update the key value of all adjacent vertices of u. 
To update the key values, iterate through all adjacent vertices. F
or every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value as the weight of u-v
"""

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # weight 
        
        """
        Algorithm --> visitd set, heap to keep minimum weight distance 
        Prim, 
        distance of infinity vector of n, 
        add the first point 0, 0 index
        mst set, 
        queue --> while 
          pop the min distance using heapq
          if not in mst add it to queue 
          check all the non visited neighbors, update the distance 
        """
        res = 0
        n = len(points)
        q = [(0, 0)]
        dist = [float('inf')]*n
        mst = set()
        while q:
            # 1. pop min node which is not in mst
            w, min_idx = heapq.heappop(q)
            if min_idx in mst:
                continue # node was already added to the mst set
                
            # 2 add min node to mst
            res += w
            mst.add(min_idx)
            
            # 3. update min distance for neighbors in graph if not in mst and add to heap
            for v in range(n):
                if v not in mst:
                    d = abs(points[v][0]-points[min_idx][0]) + abs(points[v][1]-points[min_idx][1])
                    if d < dist[v]:
                        dist[v] = d
                        heapq.heappush(q, (d, v))
        return res
