from datetime import datetime
import collections


"""
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
"""
class Solution:
        def isScramble(self, s1: str, s2: str) -> bool:
            """

            :param s1:
            :param s2:
            :return:

            returns True if s2 is a scrambled string of s1, otherwise, returns False. Use dynamic programming.
            """
            n = len(s1)
            dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(n):
                    dp[1][i][j] = s1[i] == s2[j]
            for l in range(2, n + 1):
                for i in range(n - l + 1):
                    for j in range(n - l + 1):
                        for k in range(1, l):
                            if dp[k][i][j] and dp[l - k][i + k][j + k] or dp[k][i][j + l - k] and dp[l - k][i + k][j]:
                                dp[l][i][j] = True
                                break
            return dp[n][0][0]



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.isScramble([100,200],150))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))