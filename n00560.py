
from datetime import datetime
import bisect

import bisect
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        hash = {0:1}
        ans = 0
        s = 0
        for n in nums:
            if s - k + n in hash:
                ans += hash[s - k + n]
            s += n
            if s in hash:
                hash[s] += 1
            else:
                hash[s] = 1
        return ans






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.subarraySum([1,1,1], 2))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))