
from datetime import datetime
import bisect

import numpy as np


class Solution:
    def generateParenthesis(self, n: int):
        global hash
        hash = {1: ['()'], 0: [""], 2: ["()()", "(())"]}

        def gen(n):
            if n in hash:
                return hash[n]
            else:

                gen(n - 1)
                hash[n] = []
                for i in range(n):
                    for l1 in hash[i]:
                        for l2 in hash[n - i - 1]:
                            hash[n].append("()" + l1 + l2)
                            hash[n].append("()" + l2 + l1)
                            hash[n].append(l1 + "()" + l2)
                            hash[n].append(l2 + "()" + l1)
                            hash[n].append(l1 + l2 + "()")
                            hash[n].append(l2 + l1 + "()")

                            hash[n].append("(" + l1 + ")" + l2)
                            hash[n].append("(" + l2 + ")" + l1)
                            hash[n].append(l1 + "(" + l2 + ")")
                            hash[n].append(l2 + "(" + l1 + ")")

                            hash[n].append("(" + l1 + l2 + ")")
                            hash[n].append("(" + l2 + l1 + ")")
                ans_set = set(hash[n])
                hash[n] = list(ans_set)

            return hash[n]

        return gen(n)






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.earliestFullBloom("a", "aa"))
    #print(sol.earliestFullBloom("ab", "b"))
    print(sol.generateParenthesis(4))
    #print(sol.countSubarrays([2,1,4,3,5], 10))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))