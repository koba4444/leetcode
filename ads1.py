c = int(input().strip())
x = int(input().strip())
y = int(input().strip())
ans = 0
s = 0
while True:
    ans += 1
    s += x
    if s >= c:
        print(ans)
        break
    s -= y