
from datetime import datetime
import bisect

import bisect
class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        nsort = sorted(nums[:k])
        ans.append(nsort[-1])
        for i in range(k, len(nums)):
            left = nums[i-k]
            ind = bisect.bisect_left(nsort, left)
            nsort.pop(ind)
            bisect.insort_left(nsort, nums[i])
            ans.append(nsort[-1])



        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))