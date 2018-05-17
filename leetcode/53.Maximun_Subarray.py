"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
# constraints :
# idea : kadane algorithms 

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_sum_yet = nums[0]
        cur_sum = nums[0]
        for val in nums[1:]:
            cur_sum = max(val, cur_sum+val)
            max_sum_yet = max(cur_sum, max_sum_yet)
        return max_sum_yet
