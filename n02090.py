
from datetime import datetime
import bisect

import bisect
class Solution:
    def getAverages(self, nums, k: int) -> int:
        l = len(nums)
        ans = []
        s = None
        s_int = None
        for i, n in enumerate(nums):
            if 0 > i - k or i + k > l - 1:
                ans.append(-1)
                continue
            if s == None:
                s_int = sum(nums[:2 * k + 1])
                s = s_int // (2 * k + 1)
                ans.append(s)
            else:
                s_int = s_int + nums[i + k] - nums[i - k - 1]
                s = (s_int) // (2 * k + 1)
                ans.append(s)
        return ans






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    print(sol.getAverages([6643,3914,1918,9122,3503,4072,8633,5893,952,4377,1052,4513,3157,9894,9102,8734,9068,2121,4098,5039,5698,5224,2797,5440,1541,9419,9475,4465,5490,159,829,5701,314],5))
    #print(sol.getAverages([1,1,1], 2))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))