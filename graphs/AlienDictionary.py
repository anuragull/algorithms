def find_order(words):
  
  """
  problem : Given a sorted dictionary (array of words) of an alien language, find order of characters in the language
  Solution:
  1. find a graph of adjaceny list, find the zip of i, i+1 words, zip the chars for i and i + 1, the char in the first one appends to second one
  
  2. DFS, 
    a. check for cycle 
    b. seen set has status of the node 
    c. check for each neighbor 
   
  3. Complexity : O(V + E) + O(n*m)
  
  """
  
  # find all the unique chars
        chrs = set(c for word in words for c in word)
        adj_list = {c:[] for c in chrs}

    
        # we find the edges  
        for f, s in zip(words, words[1:]):
            for c, d in zip(f, s):
                if c != d: 
                    adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(s) < len(f): 
                    return ""
                  
        # Step 2: Depth-first search.
        seen = {} 
        output = []
        
        
        def visit(node):  # Return True if there are no cycles.
            if node in seen:
                return seen[node]
            seen[node] = False # Mark node as grey.
            # search 
            for next_node in adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False 
            seen[node] = True 
            output.append(node)
            return True

        if not all(visit(node) for node in adj_list):
            return ""

        return "".join(output)
