
from datetime import datetime
import collections


class Solution:
    def containsDuplicate(self, nums):
        hash = {}
        for w in nums:
            if w in hash:
                return True

            else:
                hash[w] = 1
        return False


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.containsNearbyDuplicate([1, 2, 3, 1],3))
    print(sol.containsDuplicate([1,2,3,1]))
    #print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))