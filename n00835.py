import numpy as np



from datetime import datetime
import bisect


class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0
        a1 = np.array(img1, dtype=bool)
        a2 = np.array(img2, dtype=bool)
        for i in range(n):
            for j in range(n):
                s = sum(sum(a1[:n-i, :n-j] * a2[i:, j:]))
                if s > ans: ans = s
                s = sum(sum(a2[:n-i, :n-j] * a1[i:, j:]))
                if s > ans: ans = s
                s = sum(sum(a1[:n-i, j:] * a2[i:, :n-j]))
                if s > ans: ans = s
                s = sum(sum(a2[:n-i, j:] * a1[i:, :n-j]))
                if s > ans: ans = s
        return ans





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.largestOverlap([[1,1,0],[0,1,0],[0,1,0]],[[0,0,0],[0,1,1],[0,0,1]]))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))