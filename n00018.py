from datetime import datetime
import collections
import numpy as np

class Solution():
    def fourSum(self, nums, target):
        nums.sort()
        cnt = collections.Counter(nums)

        def kSum(k, nums, target):
            """
            :param k: Number of summed values
            :param nums: list
            :param target: tatget value
            :return:
            """
            #if len(nums) == 0 or target < nums[0]: return []

            if k == 1:
                if len(nums) > 0 and target in cnt.keys() and target >= nums[0]:
                    a = [[target]]
                    return a
                else:
                    return []
            ans = []
            for i, n in enumerate(nums):
                tail = kSum(k-1, nums[i+1:], target - n)
                if tail == []:
                    continue
                else:
                    for t in tail:
                        a = [n]+t
                        if a not in ans:
                            ans.append(a)
            return ans


        ans = kSum(4,nums,target)
        h = dict()
        for a in ans:
            h[tuple(a)] = 1

        return [list(a) for a in h.keys()]

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
    print(sol.fourSum([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
, 8))
    #print(sol.fourSum([2,2,2,2,2], 8))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))