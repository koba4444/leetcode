from datetime import datetime
import collections
from functools import reduce


class Solution:
    def fullJustify(self, words, maxWidth):
        def words_of_stroke(words, length, maxWidth, last=False):
            blanks = maxWidth - length
            n = len(words)
            every = blanks // (n-1) if n>1 else blanks
            additional = blanks % (n-1) if n>1 else 0
            if n == 1:
                return words[0] + blanks * " "
            else:
                ans = words[0]
                for i in range(1, n):
                    if not last:
                        ans += every * " "
                        if i < additional + 1: ans += " "
                    else:
                        ans += " "
                    ans += words[i]
                if last: ans += (maxWidth-len(ans)) * " "
            return ans

        l = len(words)
        ll = [len(w) for w in words]
        answer = []
        s = 0
        i_start = -1


        for i in range(l):
            if i_start < 0: i_start = i

            if s + ll[i] <= maxWidth:
                s += ll[i]
                if s < maxWidth: s += 1
                i_end = i + 1
                if i == l-1:
                    length = reduce(lambda x, y: x + y, ll[i_start: i_end])
                    answer.append(words_of_stroke(words[i_start: i_end], int(length), maxWidth, True))
                continue
            else:
                length = reduce(lambda x, y: x + y, ll[i_start: i_end])
                answer.append(words_of_stroke(words[i_start: i_end], int(length), maxWidth))
                s = ll[i]
                if s < maxWidth: s += 1
                i_start = i
                i_end = i + 1
                if i == l-1:
                    length = reduce(lambda x, y: x + y, ll[i_start: i_end])
                    answer.append(words_of_stroke(words[i_start: i_end], int(length), maxWidth, True))

        return answer





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))