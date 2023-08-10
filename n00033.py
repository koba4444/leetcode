from typing import List
from datetime import datetime
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            ind = nums.index(target)
            return ind
        except:
            return -1

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.search([0,3,1], 3))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))