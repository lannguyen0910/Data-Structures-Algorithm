class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        
        # create graph
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "#" + word[i+1:]
                graph[pattern].append(word)

        # BFS <= shortest path
        queue = collections.deque()
        visited = set()

        queue.append((beginWord, 1))
        visited.add(beginWord)
        
        while queue:
            curr, step = queue.popleft()
            if curr == endWord:
                return step
            for i in range(len(curr)):
                pattern = curr[:i] + "#" + curr[i+1:]
                for nextWord in graph[pattern]:
                    if nextWord not in visited:
                        visited.add(nextWord)
                        queue.append((nextWord, step+1))
        
        # if cannot find endWord in wordList
        return 0
    
    
# https://leetcode.com/problems/word-ladder/discuss/2240015/Python-Solution-Using-Hashmap