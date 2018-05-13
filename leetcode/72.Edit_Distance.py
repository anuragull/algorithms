"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""


# constraints 
# test "CAD" "CADA", "C" "C", "AD" "CD"
# idea : memoniation, ensure that string index at 1, return D[len1][len2]

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)  + 1
        n = len(word2)  + 1
        d = [[0 for y in range(n)] for x in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                if i == 0:
                    d[i][j] = j 
                elif j == 0:
                    d[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(
                        d[i-1][j] + 1, #delete
                        d[i][j-1] + 1, #insert
                        d[i-1][j-1] + 1 #replace             
                    )
        return d[m-1][n-1]
