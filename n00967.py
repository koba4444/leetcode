from datetime import datetime
import collections


class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        def numSCD(digit, n, k):
            a = []
            if n == 1:
                if k > 0:
                    a = [digit + i*k for i in [-1,1] if 0 <= digit + i*k <= 9 ]
                    return a
                else:
                    a = [digit]
                    return a
            else:
                if  0<=digit - k<=9:
                    a.extend(list(map(lambda x: (digit-k) * (10 ** (n-1)) + x, numSCD(digit-k, n-1, k))))
                if  0<=digit + k<=9 and k>0:
                    a.extend(list(map(lambda x: (digit+k) * (10 ** (n-1)) + x, numSCD(digit+k, n-1, k))))
                return a
        ans = []
        for d in range(1,10):
            l = list(map(lambda x: d*(10**(n-1)) + x, numSCD(d, n-1, k)))
            ans.extend(l)
        return ans

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.numsSameConsecDiff(2, 0))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))