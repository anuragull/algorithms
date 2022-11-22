def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Problem : https://leetcode.com/problems/word-ladder/
        Steps: 
        1. hash the word list
        2. queue with begin word, len = 1
        3. create a chrset 
        4. while queue
        5. pop queue, 
        6. if popped_word == endword return len
        7. loop of word, loop of charset, word[:i] + c + word[i+1:]
        8, if word in word_list, add to queue, len + 1, remove from the queue
  
        """
        # set of words
        wordList = set(wordList)
        # create a queue 
        queue = collections.deque([[beginWord, 1]])
        # all the char
        charSet = {w for word in wordList for w in word}
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in charSet:
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
