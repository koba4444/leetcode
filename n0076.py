
from datetime import datetime
import bisect


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hash = {}
        left = 0
        ans = s + t
        for l in t:
            if l in hash.keys():
                hash[l] += 1
            else:
                hash[l] = 1

        for i in range(len(s)):
            if s[i] in hash.keys():
                hash[s[i]] -= 1

                if max(hash.values()) == 0:
                    if len(ans) >= i - left + 1:
                        ans = s[left: i + 1]
                    for j in range(left, i + 1):
                        if len(ans) >= i - j + 1:
                            ans = s[j: i + 1]
                        if s[j] in hash.keys():

                            hash[s[j]] += 1
                            if max(hash.values()) > 0:
                                if len(ans) >= i - j + 1:
                                    ans = s[j : i + 1]
                                left = j+1
                                break
                            else:
                                if len(ans) >= i - j + 1:
                                    ans = s[j : i + 1]
                        else:
                            if len(ans) >= i - j + 1:
                                ans = s[j+1: i + 1]

        return "" if ans == s + t else ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minWindow("a", "aa"))
    #print(sol.minWindow("ab", "b"))
    #print(sol.minWindow("acbc", "ba"))
    print(sol.minWindow("cabwefgewcwaefgcf", "cae"))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))