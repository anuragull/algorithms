"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
#constraints : negative number
# idea : sort the first, then 
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total_len = len(nums)
        if total_len < 3:
            return []
        # sort        
        nums = sorted(nums)
        valid_values = set()
        
        solution_list = {}
        
        for i in range(total_len -2 ):
            cur_val = nums[i]
            if cur_val in valid_values:
                continue
            l = i + 1
            r = total_len -1
            while l < r :
                
                total = cur_val + nums[l] + nums[r]
                if total == 0:
                    valid_values.add(cur_val)
                    key = "%d_%d_%d" % (cur_val, nums[l], nums[r])
                    if key not in solution_list:
                        solution_list[key] = [cur_val, nums[l], nums[r]]
                    l = l + 1
                    r = r - 1
                elif total < 0:
                    l = l+1
                else:
                    r = r - 1
        return list(solution_list.values())
