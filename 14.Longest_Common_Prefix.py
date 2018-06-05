"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 0:
            return ""
        min_len = min([len(st) for st in strs])
        
        chr = ""
        for i in range(0, min_len):
            cur_ch = strs[0][i]
            lst = [ch[i] for ch in strs if ch[i] == cur_ch]
            if len([ch[i] for ch in strs if ch[i] == cur_ch]) == len(strs):
                chr += ch[i] 
            else:
                break
        return chr
