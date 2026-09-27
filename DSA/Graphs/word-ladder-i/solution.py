from collections import defaultdict
from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        if targetWord not in wordList:
            return  0 

        neighbour = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbour[pattern].append(word)

        q = deque()
        visited = set()
        q.append(startWord)
        visited.add(startWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == targetWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neibourword in neighbour[pattern]:
                        if neibourword not in visited:
                            q.append(neibourword)
                            visited.add(neibourword)
            res +=1
        return 0




    
