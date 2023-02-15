from datetime import datetime
import numpy as np
import collections
from functools import reduce
from math import factorial

class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        a=1








if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.nextPermutation([1,2,3]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))