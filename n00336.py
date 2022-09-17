from datetime import datetime
import numpy as np



class Solution:
    def palindromePairs(self, words):

        def left_palindroms(n):
            l = len(words[n])
            for i in range(l+1):
                rest = words[n][i:]
                if rest in w1.keys():
                    curr = words[n][:i]
                    ind = words[n][:i][::-1]
                    if curr == ind and curr != "":
                        """
                        if curr in lp.keys():
                            lp[curr].append(n)
                        else:
                            lp[curr] = [n]
                        """
                        if rest[::-1] in lp1.keys():
                            lp1[rest[::-1]].append(n)
                        else:
                            lp1[rest[::-1]] = [n]
        def right_palindroms(n):
            l = len(words[n])
            for i in range(-1, l+1):
                rest = words[n][:l - i - 1]
                if rest in w1.keys():
                    curr = words[n][l-i-1:]
                    ind = words[n][l-1-i:][::-1]
                    if curr == ind and curr != "":
                        """
                        if curr in rp.keys():
                            rp[curr].append(n)
                        else:
                            rp[curr] = [n]
                        """
                        if rest[::-1] in rp1.keys():
                            rp1[rest[::-1]].append(n)
                        else:
                            rp1[rest[::-1]] = [n]
        def w_w1(n):
            """
            if words[n] in w.keys():
                w[words[n]].append(n)
            else:
                w[words[n]] = [n]
            """
            if words[n][::-1] in w1.keys():
                w1[words[n][::-1]].append(n)
            else:
                w1[words[n][::-1]] = [n]



        #lp = dict()
        lp1 = dict()
        #rp = dict()
        rp1 = dict()
        w1 = dict()
        answer = set()
        l = len(words)


        for i in range(l):
            w_w1(i)
        for i in range(l):
            left_palindroms(i)
            right_palindroms(i)


        for i in range(l):
            if words[i] in w1.keys():
                for j in w1[words[i]]:
                    if j != i: answer.add((i,j))
            if words[i] in rp1.keys():
                for j in rp1[words[i]]:
                    if j != i: answer.add((j, i))
            if words[i] in lp1.keys():
                for j in lp1[words[i]]:
                    if j != i: answer.add((i, j))

        return list(map(list, answer))


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.palindromePairs([]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))