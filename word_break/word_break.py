import sys

TEST_DICT = set(["a", "apple", "pie", "mobile","samsung","sam","sung",
                            "man","mango","icecream","and",
                             "go","i","like","ice","cream"])

def greedy_break(word):
    """ finds the first word and breaks """
    word_len = len(word)
    for i in range(0, word_len):
    	prefix = word[0:i]
	if prefix in TEST_DICT:
	    suffix = word[i:word_len]
	    if suffix in TEST_DICT:
		return prefix + " " + suffix
    return None
 	

def recursive_back(word):
    """ 
         general solution 
         check a) prefix
               b) get suffix
               c) recurse on suffix
         recursion term:
              a) word matches
              b) prefix + sub_suffix
              b) None
    """
    # if word exists in the dict return word
    if word in TEST_DICT:
        return word 
    # compute length
    word_len = len(word)
    # iterate over the words
    for i in range(1, word_len):
        prefix = word[0:i]
        if prefix in TEST_DICT:
            suffix = word[i:word_len]
	    sub_suffix = recursive_back(suffix)
            if sub_suffix is not None:
                return prefix + " " + sub_suffix
    return None 
    
memoized = {}

def dynamic_prog(word):
    """ general solution """
    # if word exists in the dict return word
    if word in TEST_DICT:
        return word
    # if word is memoized
    if word in memoized:
        return memoized[word]
   
    # compute length
    word_len = len(word)
    # iterate over the words
    for i in range(1, word_len):
        prefix = word[0:i]
        if prefix in TEST_DICT:
            suffix = word[i:word_len]
            sub_suffix = recursive_back(suffix)
            if sub_suffix is not None:
                return prefix + " " + sub_suffix
    memoized[word] = None
    return None 

  
def driver(word):
    print greedy_break(word)	     
    print recursive_back(word)
    print dynamic_prog(word)


if __name__ == "__main__":
    driver("applepie")
    driver("ilikesamsung")
    driver("iiiiiii")


