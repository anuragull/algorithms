"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        str_len = len(s)
        if str_len <= 1:
            return True
        
        new_str = ""
        for i in range(0, str_len):
            if s[i].isalnum():
                new_str += s[i]

        s = new_str
        str_len = len(s)
        l = 0
        r = str_len -1
        while(l <= r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            
