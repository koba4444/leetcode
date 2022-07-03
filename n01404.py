from datetime import datetime
import numpy as np
import collections


class Solution:
    def numSteps(self, s: str) -> int:
        b = int(s, base=2)
        curr = b
        answer = 0
        while curr != 1:
            if curr & 1 :
                curr += 1
                answer += 1
            else:
                curr = curr >> 1
                answer += 1
        return answer





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.numSteps("1101"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))