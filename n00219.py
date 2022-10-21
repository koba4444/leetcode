
from datetime import datetime
import collections


class Solution:
    def containsNearbyDuplicate(self, nums, k: int):
        hash = {}
        win = [i for i in nums[:k+1]]
        for w in win:
            if w in hash:
                hash[w] += 1
                if hash[w] > 1: return True
            else:
                hash[w] = 1

        for right in range(k+1, len(nums)):
            left = right - k
            hash[nums[left - 1]] -= 1
            if nums[right] in hash:
                hash[nums[right]] += 1
                if hash[nums[right]] > 1: return True
            else:
                hash[nums[right]] = 1
        return False


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.containsNearbyDuplicate([1, 2, 3, 1],3))
    print(sol.containsNearbyDuplicate([1, 0, 1, 1],1))
    #print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))