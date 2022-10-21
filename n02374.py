
from datetime import datetime
import collections


class Solution:
    def edgeScore(self, edges):

        arr = [0] * len(edges)
        m = 0

        for n in range(len(edges)):
            arr[edges[n]] += n
            if m < arr[edges[n]]: m = arr[edges[n]]
        for key, val in enumerate(arr):
            if val == m: return key




if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.edgeScore([1,2,0]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))