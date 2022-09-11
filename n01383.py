import heapq
from datetime import datetime
import collections


# Time Complexity: O(N * (logN + logK))
# Space Complexity: O(N + K)
# where N is the total number of candidates and K is the size of team
class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k):
        es = zip(efficiency, speed)
        es = sorted(es, key=lambda x: x[0], reverse=True)
        ss, ans = 0, 0
        heap = []
        for e, s in es:
            heapq.heappush(heap, s)
            ss += s
            if len(heap) > k:
                ss -= heapq.heappop(heap)
            ans = max(ans, ss * e)
        return ans % (10**9+7)


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.maxPerformance(6,[2,10,3,1,5,8], [5,4,3,9,7,2],3))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))