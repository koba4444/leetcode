
from datetime import datetime
import bisect

import numpy as np
class Solution:
    def earliestFullBloom(self, plantTime, growTime) -> int:
        l = len(plantTime)
        ans = 0
        plant = 0
        vec = [[plantTime[i],growTime[i]] for i in range(l)]
        vec.sort(key=lambda x: -x[1])
        for ind, v in enumerate(vec):
            plant += v[0]
            if plant + v[1] > ans:
                ans = plant +v[1]
        return ans






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.earliestFullBloom("a", "aa"))
    #print(sol.earliestFullBloom("ab", "b"))
    print(sol.earliestFullBloom([1,4,3], [2,3,1]))
    #print(sol.countSubarrays([2,1,4,3,5], 10))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))