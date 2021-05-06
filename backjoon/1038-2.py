import sys

n = int(input())

cnt = 0
num = 1

if n > 1022: print(-1)
else:
    while True:
        sn = str(num)
        sn_len = len(sn)
        
        for i in range(sn_len-1, 0, -1):
            if sn[i] >= sn[i-1]:
                while num % (10 ** (sn_len-i)) != 0:
                    num += 10 ** (sn_len-i-1)

        if num < 100:
            cnt += 1
                    
        if cnt == n:
            print(num)
            break
        
        num += 1