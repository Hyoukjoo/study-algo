a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    n = a // (c - b)
    n += 1
    print(n)