from datetime import datetime
import numpy as np
import collections
from functools import reduce


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            if not i in hash.keys():
                hash[i] = True
        ans = 1
        while ans in hash.keys():
            ans += 1
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.firstMissingPositive([3,4,-1,1]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))