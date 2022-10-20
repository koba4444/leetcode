
from datetime import datetime
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        ans = ''

        for n in s:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        lst = [[key, freq] for key, freq in hash.items()]
        lst.sort(key=lambda x: (-x[1]))
        for l in lst:
            ans += (l[0] * l[1])
        return str(ans)


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.frequencySort('asfaervdf;l,eorke'))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))