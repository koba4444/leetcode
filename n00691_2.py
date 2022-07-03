from datetime import datetime
import numpy as np
import collections
import sklearn
class Solution:

    def minStickers(self, stickers, target) -> int:
        max_answer = len(target)

        a = {i[0]: i[1] for i in collections.Counter(target).most_common(26)}
        b = [{j[0]: j[1] for j in collections.Counter(i).most_common(26) if j[0] in a.keys()} for i in stickers]
        m = len(a)
        n = len(b)
        mat = np.zeros((n, m), dtype=np.int16)

        res = np.zeros(m, dtype=np.int16)
        for ind, key in enumerate(a.keys()):
            res[ind] = a[key]
            for bb_ind, bb in enumerate(b):
                if key in bb.keys():
                    mat[bb_ind, ind] = bb[key]

        def permutations_reccur(a, perm_previous=None):
            l = len(a)
            answer = []

            if perm_previous is None:
                perm_previous = [[0] * l]
            for pr in perm_previous:
                for i in range(l):
                    if pr[i] + 1 <= a[i]:
                        answer.append(pr.copy())
                        answer[-1][i] += 1
                        applic_res = res - np.array(answer[-1]).dot(mat)
                        if applic_res.max() <= 0:
                            #print(koef)
                            return None

            return answer
        def permutations(a, s, previous=None):
            l = len(a)
            if previous is None:
                previous = [0] * l
            pattern = [0] * l
            ans = []
            answer = []
            if s == 0: return [previous]
            if s > 0:
                for i in range(l):
                    if a[i] > 0:
                        answer.append(previous.copy())
                        answer[-1][i] += 1
                        b = a.copy()
                        b[i] -= 1

                        ans.extend(permutations(b, s - 1, answer[-1]))
            return ans

        def squeez(mat):
            for i in range(mat.shape[0] - 1):
                for j in range(i+1, mat.shape[0]):
                    if j > mat.shape[0] - 1 or i > mat.shape[0] - 1: break
                    if (mat[i, :] <= mat[j, :]).all():
                        mat = np.delete(mat, i, 0)
                    if j > mat.shape[0] - 1 or i > mat.shape[0] - 1: break
                    if (mat[i, :] >= mat[j, :]).all():
                        mat = np.delete(mat, j, 0)
            return mat
        mat = squeez(mat)
        mat_ratio = np.ceil((res / mat)).astype(int)

        mat_ratio[mat_ratio == mat_ratio.min()] = 0
        mat_ratio.astype(int)

        vertical_sum = mat.sum(axis=0)
        if vertical_sum.min() == 0:
            return -1


        horison_ratio_max = mat_ratio.max(axis=1) + 1

        #mat1 = np.concatenate((mat,horison_ratio_max.reshape((mat.shape[0], 1))), axis=1)
        #mat2 = mat1[mat1[:, -1].argsort()[::-1]]
        #mat = mat2[:, :-1]
        #horison_ratio_max = mat2[:, -1]

        s = 1
        perm_previous = None
        while True:
            perm_previous = permutations_reccur(horison_ratio_max, perm_previous)
            if perm_previous is None: return s
            perm = np.array(list(set(map(tuple, perm_previous))))

            s += 1










if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    for i in range(10):
        #print(sol.minStickers(["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"],"stoodcrease"))
        print(sol.minStickers(["indicate","why","finger","star","unit","board","sister","danger","deal","bit","phrase","caught","if","other","water","huge","general","read","gold","shall","master","men","lay","party","grow","view","if","pull","together","head","thank","street","natural","pull","raise","cost","spoke","race","new","race","liquid","me","please","clear","could","reply","often","huge","old","nor"],"fhhfiyfdcwbycma"))
        #print(sol.minStickers(["among","just","people","ran","sound","son","wash","design","mark","dress","arm","lie","little","copy","develop","beauty","support","sky","tail","should","machine","few","written","board","told","flat","parent","though","material","chart","hand","wear","fresh","teach","general","wont","word","third","light","region","hunt","cover","together","crease","sand","paragraph","teeth","position","whole","top"],"placeclock"))

        #print(sol.minStickers(["right","ten","year","share","period","paper","expect","village","home","happen","ring","sat","even","afraid","paint","self","range","camp","note","read","paragraph","run","basic","fill","week","his","star","power","any","colony","object","free","dark","said","chick","true","glad","child","room","lost","am","cry","quiet","crease","while","race","fun","found","dream","once"],"materialhalf"))
        #print(sol.minStickers(["gone","dont","bell","simple","colony","mine","carry","sleep","village","ready","ground","sell","use","lead","doctor","stretch","less","except","long","why","indicate","live","animal","blow","inch","got","include","hope","real","then","string","degree","syllable","blue","stop","job","key","class","he","valley","did","country","space","heat","collect","truck","mother","problem","toward","my"],"bringmethod"))
        #print(sol.minStickers(["these","guess","about","garden","him"], "atomher"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))