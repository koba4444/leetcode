from datetime import datetime
import numpy as np
import collections


class Solution:

    def minStickers(self, stickers, target) -> int:
        max_reccurtion = len(target)
        reccurtion_counter = 0
        def min_sticks_forward(stickers, target):
            m = np.zeros((len(stickers), 26), dtype=np.int8)
            map = np.zeros((len(stickers), 26), dtype=np.float64)
            nonlocal reccurtion_counter
            answer = 0
            a = {i[0]: i[1] for i in collections.Counter(target).most_common(26)}
            trg = np.zeros((26), dtype=np.int8)
            for p in a.keys():
                trg[hash_[p]] = a[p]
            curr = trg.copy()
            if curr.sum() == 0:
                return 0
            for ind, j in enumerate(b):
                for p in j.keys():
                    if curr[hash_[p]] > 0:
                        m[ind, hash_[p]] = j[p]
                        map[ind, hash_[p]] = min(j[p] / curr[hash_[p]], 1)
            map_sum = map.sum(axis=1)
            if max(map_sum) < 10 ** (-8):
                reccurtion_counter -= 1
                return -1
            # opt_ind = np.argwhere(map_sum == np.amax(map_sum)).flatten().tolist()
            opt_ind = np.argwhere(map_sum > 0.001).flatten().tolist()
            # opt_ind = list(range(len(map_sum)))
            ans_min = len(curr)
            for case in opt_ind:
                #print(stickers[case], reccurtion_counter)
                curr1 = np.maximum(0, curr - m[case])
                curr_text = ""
                for ind_n, n in enumerate(curr1):
                    curr_text += ethalon[ind_n] * n
                # print("vvvvvvvv")
                reccurtion_counter += 1
                ans = self.minStickers(stickers, curr_text)
                if ans == -1:
                    reccurtion_counter -= 1
                    return -1
                if ans < ans_min:
                    ans_min = ans
            answer += ans_min + 1
            return answer



        ethalon = "abcdefghijklmnopqrstuvwxyz"
        hash_ = {l: ethalon.index(l) for l in ethalon}
        b = [{j[0]: j[1] for j in collections.Counter(i).most_common(26)} for i in stickers]
        m = np.zeros((len(stickers), 26), dtype=np.int8)
        map = np.zeros((len(stickers), 26), dtype=np.float64)


        answer = min_sticks_forward(stickers, target)
        return answer





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.minStickers(["swim","love","father","shape","rich","multiply","new","fill","history"], "operateform"))
    #print(sol.minStickers(["notice","possible"], "basicbasic"))
    #print(sol.minStickers(["with","example","science"], "thehat"))
    #print(sol.minStickers(["these","guess","about","garden","him"], "atomher"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))