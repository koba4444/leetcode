from datetime import datetime
import collections


class Solution:
    def largestRectangleArea(self, heights) -> int:

        ans = []
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))