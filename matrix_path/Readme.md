# Problem Statement
 Lets say given a 2D matrix of size N,N we need to find shortest path to reach 0,0 to N,N.

Constraints : we can only move right and down

# Solutions
1. Greedy : find the lowest cost path and keep moving
2. DP : build the solution bottom,
   1. First set the top and left column
   2. fill up the next value as X[i][j] + min(X[1-i][j], X[i][j-1])
   3. Printing path, trace the step backwards

# Extensions

1. Add weight: Add some weights
2. Print the path: Print the optimal path
3. Add barriers : we will have infeasible path points. This would require some back tracking.
