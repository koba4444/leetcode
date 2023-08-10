from datetime import datetime
import collections



class Solution:
    def minCut(self, s: str) -> int:

        def isPalindrome(s):
            return s == s[::-1]

        if isPalindrome(s):
            return 0

        n = len(s)
        dp = [0] * n
        for i in range(n):
            dp[i] = i
            if isPalindrome(s[:i+1]):
                dp[i] = 0
                continue
            for j in range(i):
                if isPalindrome(s[j+1:i+1]):
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.minCut("aab"))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))