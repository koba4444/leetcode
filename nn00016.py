
from datetime import datetime
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.threeSumClosest([2,0,1,-4, -3], 1))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))