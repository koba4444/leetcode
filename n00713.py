
from datetime import datetime
import bisect

import bisect
class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        ans = 0
        curr_left = 0
        s = 1
        for i, n in enumerate(nums):
            s *= n
            if s < k:
                ans += i - curr_left + 1
            else:
                while s >= k:
                    if curr_left <= i:
                        s /= nums[curr_left]
                        curr_left += 1
                    else:
                        break

                ans += i - curr_left + 1
        return ans






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.numSubarrayProductLessThanK([1,2,3],0))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))