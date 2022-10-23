
from datetime import datetime
import bisect


class Solution:
    def findErrorNums(self, nums):
        l = len(nums)
        ans = [None, None]
        hash = {i + 1:0 for i in range(l)}
        for n in nums:
            hash[n] += 1
        for i in range(l):
            if hash[i + 1] == 2:
                ans[0] = i+1
            elif hash[i + 1] == 0:
                ans[1] = i+1


        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.findErrorNums([1,2,2,4]))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))