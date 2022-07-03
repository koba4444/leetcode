

from datetime import datetime


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        #print(s)
        passSign = 0
        answer = ""
        if s in ["", "+", "-"]: return 0
        if s[0] == "+":
            answer = ""
            passSign = 1
        elif s[0] == "-":
            answer = s[0]
            passSign = 1
        while passSign <= len(s) - 1 and s[passSign] in "0123456789":
            answer += s[passSign]
            passSign += 1
        if answer in ["+", "-", ""]: answer = 0
        if int(answer) < -2 ** 31: answer = -2 ** 31
        if int(answer) > 2 ** 31 - 1: answer = 2 ** 31 - 1
        return int(answer)

if __name__ == "__main__":
    sol = Solution()

    start_time = datetime.now()
    print(sol.myAtoi("00000-42a1234"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))