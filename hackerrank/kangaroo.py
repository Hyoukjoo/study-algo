x1, v1, x2, v2 = map(int, input().split())

if v1 <= v2:
    print('NO')
else:
    while True:
        x1 += v1
        x2 += v2
        if x1 == x2: 
            print('YES')
            break
        elif x1 > x2:
            print('NO')
            break