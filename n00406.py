from datetime import datetime
import numpy as np
import collections


class Solution:
    def reconstructQueue(self, people):
        people_sorted = sorted(people, key=(lambda x: (x[0], -x[1])))
        free_places = [i for i in range(len(people))]
        #weights = [i[0] for i in people]
        #a =np.array(collections.Counter(weights))
        answer = [None for i in range(len(people))]
        for p in people_sorted:
            seek = True
            i = 0
            while seek:
                ind = free_places[p[1]]
                if answer[ind + i] is None:
                    answer[ind + i] = p
                    for k in range(p[1], len(people)-1):
                        free_places[k] = free_places[k+1]
                    seek = False
                else:
                    i += 1
        return answer





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.reconstructQueue([[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))