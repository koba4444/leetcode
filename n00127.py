from datetime import datetime
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

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


        wordSet = set(wordList)
        level = 0
        byLevel = [[beginWord]]
        while True:
            if len(wordSet) == 0: return 0
            for ind, w in enumerate(byLevel[level]):
                if diffOneLetter(w, endWord) and endWord in wordSet: return level + 2
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


    print(sol.ladderLength("hot", "dog", ["hot","dog"]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))