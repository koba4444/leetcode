from datetime import datetime
import collections


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                proxy = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = proxy
        for i in range(n):
            for j in range(n // 2):
                proxy = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = proxy


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))