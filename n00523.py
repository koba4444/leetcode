
from datetime import datetime
import bisect

import bisect
class Solution:
    def checkSubarraySum(self, nums, k: int):
        hash = {}
        s = 0
        zeros_one_by_one = 0
        if len(nums) < 2: return False
        if (nums[0] + nums[1]) % k == 0:
            return True
        else:
            hash[0] = 1
        for i in range(len(nums)):
            if nums[i] % k == 0:
                zeros_one_by_one += 1
                if zeros_one_by_one == 2:
                    return True
                else:
                    continue
            else:
                zeros_one_by_one = 0
            s += nums[i]
            s = s % k
            if s in hash:
                return True
            else:
                hash[s] = 1
        return False






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.checkSubarraySum([1,2,12], 6))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))