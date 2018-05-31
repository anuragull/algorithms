"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


"""

class Solution:
    def wordBreak(self, word, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not word or not wordDict:
            return False
        last_len = [-1] * len(word)
        for i in range(len(word)):
            # if the word is dict
            if word[:i+1] in wordDict:
                last_len[i] = i + 1
            
            if last_len[i] == -1:
                # decompose into smaller unit
                for j in range(i):
                    # see if the last valid word, (prefix) and see if the suffix is in dict
                    if last_len[j] != -1 and word[j+1:i+1] in wordDict:
                        # at this position it can be broken
                        last_len[i] = i -j
                        break
        if last_len[-1] != -1:
            return True
        else:
            return False      
    
