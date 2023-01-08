from datetime import datetime
import collections


class Solution:
    def maxPoints(self, points) -> int:
        hash = {}

        answer = 0
        for i, val_1 in enumerate(points):
            if i < 1: continue
            hash_used = {}
            for j, val_2 in enumerate(points):
                if j>=i: break
                dx = (points[j][0] - points[i][0])
                if dx != 0:
                    k = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    a = points[j][1] - k * points[j][0]
                else:
                    k = "inf"
                    a = points[j][0]
                ind = tuple((k, a))
                if not ind in hash_used.keys():
                    if ind in hash.keys():
                        hash[ind] += 1
                        hash_used[ind] = True
                    else:
                        hash[ind] = 1
                        hash_used[ind] = True
                    if answer < hash[ind]:
                        answer = hash[ind]
        return answer + 1



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))