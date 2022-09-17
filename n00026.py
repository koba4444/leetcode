from datetime import datetime
import collections


class Solution:
    def removeDuplicates(self, nums):
        count = 0
        j = 0
        for i in range(len(nums)):
            if i > j and nums[i] == nums[j]:
                continue
            else:
                if nums[i] > nums[j]:
                    nums[j+1] = nums[i]
                    j += 1

        return j + 1


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    #print(sol.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))