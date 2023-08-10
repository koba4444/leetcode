from typing import List
from datetime import datetime

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for step in range(len(nums)):
            if nums[ind] == 0:
                nums.pop(ind)
                nums.append(0)
            else:
                ind += 1



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.moveZeroes([0,0,1]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))