"""
Word Ladder -  LeetCode #127
Find the length of shortest transformation sequence from beginWord to endWord.
"""

from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet: return 0
    q = deque([(beginWord, 1)])
    while q:
        word, steps = q.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + c + word[i+1:]
                if nxt in wordSet:
                    wordSet.remove(nxt)
                    q.append((nxt, steps+1))
    return 0

# Test
print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))  # 5
