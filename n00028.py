from datetime import datetime
from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        ans = -1
        for i in range(l1 - l2 + 1):
            for j in range(l2):
                if needle[j] != haystack[i+j]:
                    break
                if j == l2 - 1:
                    ans = i
            if ans != -1:
                return ans
        return ans



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.strStr("hello", "ll" ))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))