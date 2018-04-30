import itertools
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(nums):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
