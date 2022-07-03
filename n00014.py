from datetime import datetime
import collections


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = strs[0]
        for w in strs[1:]:
            m = min(len(w), len(ans))
            for l in range(min(len(w), len(ans))):
                if w[l] != ans[l]:
                    ans = ans[:l]
                    break
            ans = ans[:m]

        return ans





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.longestCommonPrefix(["abab","aba",""]))
    #print(sol.longestCommonPrefix(["flower","flow","flight", "dd", ""]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))