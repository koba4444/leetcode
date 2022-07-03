from datetime import datetime
import numpy as np



class Solution:
    def shortestPalindrome(self, s) -> str:

        def isPalindrome(s):
            return s == s[::-1]

        answer = 0
        l = len(s)
        for i in range(l, 0,  -1):
            if isPalindrome(s[:i]):
                answer = s[i:][::-1] + s
                return answer
        return s[::-1] + s


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.shortestPalindrome("aacecaa"))
    print(sol.shortestPalindrome("caa"))
    print(sol.shortestPalindrome("cab"))
    print(sol.shortestPalindrome(""))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))