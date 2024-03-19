s = list(map(int, input().split()))
l = 0
res = {0}
left = 0
lmax = 1
print(s)
if len(s) == 0:
    print({0})
for right in range(len(s) - 1):
    if s[right+1] > s[right]:
        l += 1
        lmax = max(l, lmax)
        if len(res) == 1 or l >= lmax:
            res = {left, right+1}
    else:
        if l >= lmax:
            res = {left, right+1}
        l = 0
        left = right + 1
    print(left, right)

print(res)



