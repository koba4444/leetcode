from datetime import datetime
import collections
from decimal import *


class Solution:
    def minimumLines(self, stockPrices) -> int:
        stockPrices = sorted(stockPrices, key = (lambda x: x[0]))
        answer = 0
        k_curr = None


        for ind, point in enumerate(stockPrices):
            if ind < 1: continue

            a = Decimal(stockPrices[ind][1] - stockPrices[ind - 1][1])
            b = Decimal(stockPrices[ind][0] - stockPrices[ind - 1][0])
            k = Decimal(a / b)
            print(k)
            if k_curr == None or abs(k - k_curr) > 10 ** (-25):
                answer += 1
                k_curr = k
        return answer


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.minimumLines([[1,1],[500000000,499999999],[1000000000,999999998]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))