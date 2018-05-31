"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False

       
        str_split = str.split(" ")
        if len(pattern) != len(str_split):
            return False
        if len(pattern) == len(str_split) and len(pattern) == 1:
            return True
            
        d1 = {}
        d2 = {}
        for i, ch in enumerate(pattern):
            word = str_split[i]
            if ch not in d1:
                if word not in d2:
                    d1[ch] = word
                    d2[word] = ch
                elif d2[word] != ch:
                    return False             
            elif d1[ch] != word:
                return False
        return True

