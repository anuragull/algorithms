"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""


# constraint sign
# idea : get the denominator . multiply by 10, and keep adding the remainder 
import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        x = abs(x)
        reverse = 0
        while x != 0:
            rem = x % 10
            reverse = reverse * 10 + rem
            x = int(x /10)
        val = sign * reverse
        if val > pow(2, 31) -1 or val < - pow(2,31):
            return 0
        return sign * reverse
            
