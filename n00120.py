from datetime import datetime
import collections


class Solution:
    def minimumTotal(self, triangle) -> int:
        l = len(triangle)
        for i in range(1, l):
            print("before: ", triangle[l - 1 - i])
            for j in range(len(triangle[l - i - 1])):
                triangle[l - 1 - i][j] = triangle[l - 1 - i][j] + min(triangle[l - i][j], triangle[l - i][j + 1])
            print("after: ", triangle[l - 1 - i])
        return triangle[0][0]

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))