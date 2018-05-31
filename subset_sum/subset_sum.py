import sys

def test_subset_sum(arr, target):
    n = len(arr)

    dp = [[True for x in range(target + 1)] for y in range(n+1)]

    print(len(dp))
    # base case 
    for i in range(0, n+1):
        dp[i][0] = True

    # XXX
    for i in range(1, target + 1) :
        dp[0][i] = False

    # Fill the subset table in botton 
    # up manner
    for i in range(1, n+1) :
        for j in range(1, target+1) :
            # current value is lees than last unit, get the state of the
            # previous
            if(j < arr[i-1]) :
                dp[i][j] = dp[i-1][j]
            # else is either the previous or j - previous entry
            if (j >= arr[i-1]) :
                dp[i][j] = dp[i-1][j] or dp[i - 1][j-arr[i-1]]
   
    return dp[n][target];
if __name__ == "__main__":
    arr = [2,3,4, 5]
    target = 8
    print(test_subset_sum(arr, target))
