def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    cur_sum = nums[0]
    for val in nums[1:]:
        cur_sum = max(val, cur_sum + val)
        max_sum = max(cur_sum, max_sum)
    return max_sum

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
