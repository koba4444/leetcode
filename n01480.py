from datetime import datetime
import collections


class Solution:
    def runningSum(self, nums):
        ans = [nums[0]]
        for i in nums[1:]:
            ans.append(i + ans[-1])
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.runningSum([1,2,3,4,5]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))