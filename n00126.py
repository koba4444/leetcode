from datetime import datetime
import collections

class Node():
    def __init__(self, val="", next=[], previous=None):
        self.val = val
        self.next = next

    def chain(self):
        ans = []
        node = self
        while node.previous != None:
            ans = ans.append(node.val)
        return ans[::-1]


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):

        def diffOneLetter(w1, w2):
            diff = 0
            for ind, l in enumerate(list(w1)):
                if l != w2[ind]:
                    diff += 1
                    if diff > 1: return False
            if diff == 1:
                return True
            else:
                return False

        answer = []
        wordSet = set(wordList)
        level = 0
        root = Node(beginWord)
        while True:
            if len(wordList) == 0: return 0
            for ind, w in enumerate(byLevel[level]):
                if diffOneLetter(w, endWord) and endWord in wordList: return level + 2
                for s in wordSet:
                    if diffOneLetter(w, s):
                        if len(byLevel) == level + 1:
                            byLevel.append([s])
                        else:
                            byLevel[level + 1].append(s)
                        ss = {s}
                        wordSet = wordSet - ss


            level += 1
            if len(byLevel) < level + 1:
                return 0


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()


    print(sol.findLadders("hot", "dog", ["hot","dog"]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))