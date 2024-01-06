from datetime import datetime
import numpy as np



#-----------
class Solution:
    def maximalRectangle(self, matrix) -> int:

        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [500] * n
        right = [-1] * n
        height = [0] * n
        maxRectRightUpperCoords = [0] * n
        maxA = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):
                for k in range(j,n):
                    if height[k] == 0: break
                    maxA = max(maxA, (k - j + 1) * (0 if j == k else min(height[j:k])))

        return maxA










if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.maximalRectangle(
        [["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]))
    print(sol.maximalRectangle(
        [["1","0","0","0","1"],["1","1","0","1","1"],["1","1","1","1","1"],["0","0","1","0","0"]]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))