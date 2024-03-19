s = list(map(str, input().split()))
hash = {}
start = 0
l = len(s)
res = [0,0]
#             V
# a s d a s d f
#       ^


for right in range(l):
    if s[right] in hash.keys() and hash[s[right]] >= start:
        if right - start > res[1] - res[0] - 1:
            res = [start, right]
        start = hash[s[right]] + 1
        hash[s[right]] = right
    elif s[right] in hash.keys() and hash[s[right]] < start:
        hash[s[right]] = right
        if right - start > res[1] - res[0] - 1:
            res = [start, right + 1]
    elif ~(s[right] in hash.keys()):
        hash[s[right]] = right
        if right - start > res[1] - res[0] - 1:
            res = [start, right + 1]
print(s[res[0]:res[1]])





