from datetime import datetime
import collections


class Solution:
    def transpose(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        ans = [[0 for i in range(rows)] for j in range(columns)]
        for r in range(rows):
            for c in range(columns):
                ans[c][r] = matrix[r][c]
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))