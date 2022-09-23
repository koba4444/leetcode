from datetime import datetime
import collections


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        s = ""
        for i in range(n):
            a = bin(i+1)[2:]
            s += a

        return(int(s, 2) % mod)



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.concatenatedBinary(3))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))