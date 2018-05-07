
import sys

def match(a, b):
    return 1

def each_edit(dp, str1, str2, i, j, trans=True):
    if i == 0:
        dp[i][j] = j
    elif j == 0:
        dp[i][j] = i
    elif (str1[i-1] == str2[j-1]):
        dp[i][j] = dp[i-1][j-1]
    else:
        min_list = [
           dp[i][j-1] + 1,
           # insertion
           dp[i-1][j] + 1,
           # substitution
           dp[i-1][j-1] + match(str1[i-1], str2[j-1])
        ]
        if trans and i > 1 and j > 1 and str1[i-1] == str2[j-2] and str2[j-1] == str1[i-2]:
            min_list.append(dp[i-2][j-2] + 1)
        dp[i][j] = min(min_list)

     

def get_edit_dist(str1, str2):
    len1 = len(str1) + 1
    len2 = len(str2) + 1
    #print(len1, len2)
    #print(str1, str2)
    dp = [[0 for y in range(len2)] for x in range(len1)]
    # init row edit between an empty string

    # compute the edits
    for i in range(len1):
        for j in range(len2):
	    each_edit(dp, str1, str2, i, j, True)	    
	    continue
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif (str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
		min_list = [
		    dp[i][j-1] + 1,
                    # insertion
                    dp[i-1][j] + 1,
                    # substitution
                    dp[i-1][j-1] + match(str1[i-1], str2[j-1])
		]
                #if i > 1 and j > 1 and str1[i-1] == str2[j-2] and str2[j-1] == str1[i-2]:
		#    min_list.append(dp[i-2][j-2] + 1)
	        dp[i][j] = min(min_list)
	 	
	

    return dp[len1-1][len2-1]


if __name__ == '__main__':
    dist = get_edit_dist(sys.argv[1], sys.argv[2])
    print("The edit dist between %s and %s is %d" %(sys.argv[1], sys.argv[2], dist))


