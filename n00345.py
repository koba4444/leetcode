
from datetime import datetime
import bisect

import numpy as np


class Solution:
    def reverseVowels(self, s: str) -> str:

        left = 0
        right = len(s) - 1
        vow = "aeiouAEIOU"
        while left < right:
            if s[left] in vow:
                while left < right:
                    if s[right] in vow:
                        v1 = s[left]
                        v2 = s[right]
                        s = s[:left] + v2 + s[left + 1:right] + v1 + s[right + 1:]

                        left += 1
                        right -= 1
                        break
                    else:
                        right -= 1
            else:
                left += 1
        return s






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.earliestFullBloom("a", "aa"))
    #print(sol.earliestFullBloom("ab", "b"))
    print(sol.generateParenthesis(4))
    #print(sol.countSubarrays([2,1,4,3,5], 10))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))