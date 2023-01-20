from datetime import datetime
import collections
from functools import reduce


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        rec = {0:0}
        answer = 0
        counter = 0
        for i in range(len(s)):
            if s[i] == '(':
                counter += 1
                if not counter in rec.keys() or rec[counter] == -1:
                    rec[counter] = i + 1

            elif s[i] == ')':
                counter -= 1
                rec[counter + 1] = -1

                if counter in rec.keys():
                    if answer < i - rec[counter] + 1:
                        answer = i - rec[counter] + 1
                else:
                    rec[counter] = i + 1
        return answer




if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.longestValidParentheses("()(()"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))