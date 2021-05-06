import sys

input = sys.stdin.readline

n = int(input())

i = 0
cnt = 0
flag = False
    
for i in range(1, int(1e6)):
    if i <= 10:
        cnt += 1
        if i == n:
            print(i)
            break
    else:
        str_n = str(i)
        size = len(str_n)
        is_decrease = True
        
        for s in range(size - 1):
            if str_n[s] <= str_n[s+1]:
                is_decrease = False
                break
            
        if is_decrease: 
            cnt += 1
    
    if cnt == n:
        print(i)
        flag = True
        break

if not flag:
    print(-1)