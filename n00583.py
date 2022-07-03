from datetime import datetime
import numpy as np


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        shifts = np.zeros((l1,l2), dtype=np.int16)
        for i1 in range(l1):
            for i2 in range(l2):
                for letter in d.keys():
                    if i1==0 and i2 == 0:
                        shifts[i1,i2] = (word1[i1] == word2[i2])
                    else:
                        if word1[i1] == word2[i2]:
                            shifts[i1,i2] = 1 if (i1 == 0 or i2 == 0) else shifts[i1-1, i2-1] + 1
                        else:
                            shifts[i1, i2] = max(0 if i1 == 0 else shifts[i1-1, i2], 0 if i2 == 0 else shifts[i1, i2-1])
        return l1 + l2 - 2 * shifts[l1-1, l2-1]


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minDistance("alewetb", "lewet",))
    print(sol.minDistance("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef","bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))