from datetime import datetime
import collections


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        answer = 0
        if target == 1: return 0
        curr = target
        doubles_retained = maxDoubles
        while curr > 1:
            if curr % 2 == 1:
                answer += 1
                curr -= 1
            else:
                if doubles_retained > 0:
                    doubles_retained -= 1
                    answer += 1
                    curr //= 2
                else:
                    answer += (curr-1)
                    return answer
        return answer


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.minMoves(5,0))
    print(sol.minMoves(19,2))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))