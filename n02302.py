
from datetime import datetime
import bisect

import bisect
class Solution:
    def countSubarrays(self, nums, k: int) -> int:
        ans = 0
        curr_left = 0
        s = 0
        for i, n in enumerate(nums):
            s = (s / max(i - curr_left, 1) + nums[i]) * (i - curr_left + 1)
            if s < k:
                ans += i - curr_left + 1
            else:
                while s >= k:
                    if curr_left <= i:
                        s = (s / (i - curr_left + 1) - nums[curr_left]) * (i - curr_left)
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
    print(sol.countSubarrays([1,1,1], 5))
    #print(sol.countSubarrays([2,1,4,3,5], 10))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))