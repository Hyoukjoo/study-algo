s, e = map(int, input().split())

cnt = 0
res = 0
i = 1
while True:
    for _ in range(i):
        cnt += 1
        if cnt > e:
            print(res)
            exit()
        if s <= cnt:
            res += i
    i += 1