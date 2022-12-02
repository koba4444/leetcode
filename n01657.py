class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1 = {}
        h2 = {}
        for i in word1:
            if i in h1.keys():
                h1[i] += 1
            else:
                h1[i] = 1
        for i in word2:
            if i in h2.keys():
                h2[i] += 1
            else:
                h2[i] = 1
        if len(h1) != len(h2): return False
        if set(h1.keys()) != set(h2.keys()): return False

        h = zip(sorted(list(h1.values())), sorted(list(h2.values())))

        if max([abs(x[0] - x[1]) for x in h]) == 0:
            return True
        else:
            return False

from datetime import datetime
import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1 = {}
        h2 = {}
        for i in word1:
            if i in h1.keys():
                h1[i] += 1
            else:
                h1[i] = 1
        for i in word2:
            if i in h2.keys():
                h2[i] += 1
            else:
                h2[i] = 1
        if len(h1) != len(h2): return False
        if set(h1.keys()) != set(h2.keys()): return False

        h = zip(sorted(list(h1.values())), sorted(list(h2.values())))

        if max([abs(x[0] - x[1]) for x in h]) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.closeStrings('abc', 'cab'))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))