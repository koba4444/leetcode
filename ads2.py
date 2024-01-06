x = int(input().strip())
y = int(input().strip())
n = int(input().strip())

def fib_n_and_nplus1(n):
    v = [1, 1]
    for i in range(n):
        v.append(v[-1]+v[-2])
    return v[n-2], v[n-1]


if n == 1:
    print(x)
elif n == 2:
    print(y)
else:
    a,b = fib_n_and_nplus1(n)
    print(a * y + b * x)