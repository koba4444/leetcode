from datetime import datetime
import collections


class Solution:


    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        global tree
        tree = {}
        for ind, val in enumerate(manager):
            if val not in tree.keys():
                tree[val] = [ind]
            else:
                tree[val].append(ind)
        a = 1
        def time_needed(vert, informTime):
            #print(tree[vert] if vert in tree.keys() else "end")
            if vert in tree.keys():
                m = 0
                for i in tree[vert]:
                    #print("i=", i)
                    s = time_needed(i, informTime)
                    if m < informTime[i] + s:
                        m = informTime[i] + s
                return m
            else:
                return 0

        return (time_needed(-1, informTime))

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]))
    #print(sol.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,21,0,0,0]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))