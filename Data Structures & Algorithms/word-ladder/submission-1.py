class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        
        maps = {}

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]

                if pattern not in maps:
                    maps[pattern] = [word]
                else:
                    maps[pattern].append(word)
        
        visit = set()
        q = collections.deque()
        q.append(beginWord)
        visit.add(beginWord)

        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    print(maps[pattern])
                    for nbr in maps[pattern]:
                        if nbr not in visit:
                            q.append(nbr)
                            visit.add(nbr)
            res += 1
        
        return 0