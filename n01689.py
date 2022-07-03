from datetime import datetime
import collections


class Solution:
    def minPartitions(self, n: str) -> int:
        answer = 0
        for i in n:
            ii = int(i)
            if ii == 9:
                return ii
            else:
                if ii > answer:
                    answer = ii
        return answer



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(minPartitions("32"))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))