# Problem statement

Given an infinite amount of coin denominations, find the minimum number of coins required to make change 

# Approaches

1. Greedy Algorithm
    1. Find the maximum, then find next maximum and so on.
2. Dynamic Programming 
    1. Table to record the minimum number of coins required at each step
        1. optimal soultion is C[j] = 1 + C[j-di]
    2. recursive define 1 + min(C[j]) where 1 <= i <= k
    3. Compute bottom up (that is compute C[1] to C[n])
3. Recursive Program
    1. recursively find the min
    2. stopping conditions are n < 0 : inf && n ==0 : 0 
    3. recursive min(func(n-di) where  1 <= i <= k

# Problem extension 

1. How many ways to make the change
2. Assuming if you have finite amount of change

# Reference

1. http://ace.cs.ohiou.edu/~razvan/courses/cs4040/lecture19.pdf
