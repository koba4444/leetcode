from datetime import datetime
import collections


class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        op = set("([{")
        cl = set(")]}")
        st = ""
        d = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in op:
                st += i
            elif i in cl:
                if len(st) == 0: return False
                if st[-1] == d[i]:
                    st = st[:-1]
                else:
                    return False
        if st == "":
            return True
        else:
            return False


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.isValid('(asf[d]rtre)'))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))