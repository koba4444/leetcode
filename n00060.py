from datetime import datetime
import numpy as np
import collections
from functools import reduce
from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        symbols = list(range(1,n+1))
        kk = k
        if n == 1: return "1"
        if n == 2: return ["12","21"][k-1]
        for i in range(n):
            if len(symbols) == 1:
                ans += str(symbols[0])
                break
            elif len(symbols) == 2:
                if kk == 1:
                    ans = ans + str(symbols[0]) + str(symbols[1])
                    break
                if kk == 2:
                    ans = ans + str(symbols[1]) + str(symbols[0])
                    break

            ind = (kk - 1) // factorial(n-i-1) if (n - i - 1 > 1 and kk > 2) else 0
            kk = kk - ind * factorial(n-i-1) if (n - i - 1 > 1 and kk > 2) else kk
            ans += str(symbols[ind])
            symbols.pop(ind)

        return ans





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.getPermutation(3,4))
    print(sol.getPermutation(3,2))
    print(sol.getPermutation(4,9))
    print(sol.getPermutation(3,1))
    print(sol.getPermutation(2,2))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))