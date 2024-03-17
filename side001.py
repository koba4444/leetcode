n,q = map(int, input().split())
print(n,q)
nums = list(map(int,input().split()))
pre = [0]
for i in range(n):
    pre += [pre[-1]+nums[i]]


print(nums)
print(pre)

for i in range(q):
    l, r = map(int, input().split())
    nums[l] += 1
    if r+1 < n:
        nums[r+1] -= 1
print(nums)
pre1 = [0]
for i in range(n):
    pre1 += [pre1[-1] + nums[i]]
print(pre1)
for i in range(1, n+1):
    nums[i-1] = pre1[i] - pre[i-1]
print(nums)

