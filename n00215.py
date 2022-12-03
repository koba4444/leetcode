
from datetime import datetime



class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return sorted(nums, key=lambda x: -x)[k - 1]


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.findKthLargest([1,2,1,2,3,4,3,2,3],2))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))