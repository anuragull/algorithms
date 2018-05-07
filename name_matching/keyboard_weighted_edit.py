
import sys

KEYMATCH = {
'q' : (0,0),
'w' : (0,1),
'e' : (0,2),
'r' : (0,3),
't' : (0,4),
'y' : (0,5),
'u' : (0,6),
'i' : (0,7),
'o' : (0,8),
'p' : (0,9),
'a' : (1,0),
's' : (1,1),
'd' : (1,2),
'f' : (1,3),
'g' : (1,4),
'h' : (1,5),
'j' : (1,6),
'k' : (1,7),
'l' : (2,8),
'z' : (2,0),
'x' : (2,1),
'c' : (2,2),
'v' : (2,3),
'b' : (2,4),
'n' : (2,5),
'm' : (2,6)
	
}

def match(a, b):
    a = a.lower()
    b = b.lower()
    dist = abs(KEYMATCH[a][0] - KEYMATCH[b][0]) + abs(KEYMATCH[a][1] - KEYMATCH[b][1])
    return dist

def each_edit(dp, str1, str2, i, j):
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
        dp[i][j] = min(min_list)

def get_edit_dist(str1, str2):
    len1 = len(str1) + 1
    len2 = len(str2) + 1
    dp = [[0 for y in range(len2)] for x in range(len1)]
    # compute the edits
    for i in range(len1):
        for j in range(len2):
	    each_edit(dp, str1, str2, i, j, False)	    

    return dp[len1-1][len2-1]


if __name__ == '__main__':
    dist = get_edit_dist(sys.argv[1], sys.argv[2])
    print("The edit dist between %s and %s is %d" %(sys.argv[1], sys.argv[2], dist))


