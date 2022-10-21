
from datetime import datetime
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, valueDiff):
        win = [i for i in nums[:k+1]]
        win.sort()
        for i in range(1,len(win)):
            if abs(win[i] - win[i-1]) <= valueDiff:
                return True


        for right in range(k+1, len(nums)):
            left = right - k
            win.remove(nums[left - 1])
            bisect.insort(win, nums[right])
            ind = win.index(nums[right])
            if ind > 0 and abs(win[ind] - win[ind - 1]) <= valueDiff: return True
            if ind < k and abs(win[ind] - win[ind + 1]) <= valueDiff: return True

        return False


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.containsNearbyDuplicate([1, 2, 3, 1],3))
    print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))