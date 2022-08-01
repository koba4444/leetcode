from datetime import datetime
import numpy as np


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        s = np.zeros((m, n), dtype=np.int64)
        if m == 1 or n == 1:
            return 1
        s[0, :] = 1
        s[:, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                s[i, j] = s[i-1, j] + s[i, j-1]
        print(s)
        return s[m-1, n-1]




if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.uniquePaths(7,7))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))