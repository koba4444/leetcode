
from datetime import datetime
import bisect


class Solution:
    def findDuplicate(self, nums) -> int:
        l = len(nums)
        ans = [None, None]
        hash = {i + 1:0 for i in range(l)}
        for n in nums:
            hash[n] += 1
        for i in range(l):
            if hash[i + 1] >= 2:
                return i+1



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.findErrorNums([1,3,4,2,2]))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))