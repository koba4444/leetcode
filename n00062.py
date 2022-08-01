from datetime import datetime
import numpy as np


class Solution:
    global s
    s = dict()
    s[(2,2)] = 2
    def uniquePaths(self, m: int, n: int) -> int:

        if n == 1 or m == 1:
            s[(m, n)] = 1
            return 1
        if (m, n) in s.keys():
            return s[(m, n)]
        elif (n, m) in s.keys():
            return s[(n, m)]

        mm = min(m, n)
        nn = max(m, n)
        near_half = (nn) // 2
        ans = 0
        for i in range(1, mm + 1):
            u1 = (i == 1 or near_half == 1 or (self. uniquePaths(i, near_half)))
            u2 = (mm + 1 - i == 1) or (nn - near_half == 1) or (self.uniquePaths(mm + 1 - i, nn - near_half))
            ans += u1 * u2


        s[(n, m)] = ans
        #print(ans)
        return ans



        """
        mm = min(m, n)
        nn = max(m, n)
        s = np.zeros((mm, nn), dtype=np.int32)
        s[0, :] = 1
        s[:, 0] = 1
        for i in range(1, mm):
            s[i, i] = 2 * s[i-1, i]
            for j in range(i + 1, nn):
                s[i, j] = s[i - 1, j] + s[i, j - 1]
        print(s)
        return s[mm- 1, nn - 1]
        """



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.uniquePaths(7, 3))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))