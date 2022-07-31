import collections
import numpy as np
a = np.array([3,2,1,5,6,6,6,6,6,6])
s = 5
b = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
def permutations(a, perm_previous=b):
    l = len(a)
    answer = []

    if perm_previous is None:
        perm_previous = [[0] * l]
    for pr in perm_previous:
        for i in range(l):
            if pr[i] + 1 <= a[i]:
                answer.append(pr.copy())
                answer[-1][i] += 1
    return answer
p = permutations(a)
ll = len(p)
print(p)
print(ll)
ss = set(map(tuple,(p)))
#print(ss)
print(len(ss))


number = 10.125
print(f"{round(number):.2f}")
