from datetime import datetime
import numpy as np


class Solution:
    global s
    s = dict()
    s[(2,2)] = 2
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            s[(m, n)] = 1
            s[(n, m)] = 1
            return 1
        if (m, n) in s.keys():
            return s[(m, n)]

        mm = min(m, n)
        nn = max(m, n)
        near_half = (nn + 1) // 2
        ans = 0
        for i in range(1, mm + 1):
            ans += (self. uniquePaths(i, near_half) *
                    self.uniquePaths(mm + 1 - i, nn - near_half)
                    )

        s[(m, n)] = ans
        s[(n, m)] = ans
        print(ans)
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
    print(sol.uniquePaths(100, 100))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))