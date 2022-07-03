from datetime import datetime
import collections


class Solution():
    def divide(self, dividend: int, divisor: int) -> int:
        print(bin(dividend))
        print(bin(divisor))
        def n_right_digits(a, n):
            res = 0
            for i in range(n):
                res += a & (1 << i)
            return res

        def max_bit_shift(a, b):
            i = 1
            while a>>i >= b:
                i += 1
            return i - 1
        def subtract(a,b, n=32):
            hold = 0
            res = 0
            if a < b: return a
            for i in range(0, n):
                mask = 1 << i
                am = (a & mask) >> (i )
                bm = (b & mask) >> (i )
                r = hold + am - bm
                if r >= 0:
                    res += r << (i )
                    hold = 0
                elif r == -1:
                    res += 1 << (i )
                    hold = -1
                elif r == -2:
                    hold = -1
            return res
        res = 0

        def abs(a):
            if a >= 0: return a
            else: return -a

        def sgn(a,b=1):
            if a >= 0 and b>= 0 or a < 0 and b < 0: return 1
            else: return -1

        def corr_sgn(a, sgn):
            if sgn == 1: return a
            else:return -a

        sgn = sgn(dividend, divisor)
        cur1 = abs(dividend)
        cur2 = abs(divisor)

        max_shift = max_bit_shift(cur1, cur2)
        for i in range(max_shift + 1):
            if cur1 >> (max_shift - i) >= cur2:
                res = (res << 1) + 1
            else:
                res = (res << 1)
            part1 = subtract(cur1 >> (max_shift - i), cur2) << (max_shift - i)
            part2 = n_right_digits(cur1, max_shift - i)
            cur1 = part1 + part2

        res = corr_sgn(res, sgn)
        if res > 2147483647: return 2147483647
        if res < -2147483648: return -2147483648

        #print(max_bit_shift(dividend, divisor))
        #print(subtract(dividend >> max_bit_shift(dividend, divisor),  divisor))
        return res


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(-2147483648, "   ", sol.divide(-2147483648, -1))
    """
    for k in range(-200, 200):
        print(k, "   ", sol.divide(k, 3))
    """
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))