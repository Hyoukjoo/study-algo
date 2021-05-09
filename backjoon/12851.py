

a, b = map(int, input().split())
vistied = [0] * 1000001
res_min = 1000001
res_cnt = 0

def dfs(n, cnt):
    global res_cnt, res_min
    
    if n == b:
        if res_min > cnt:
            res_min = cnt
            res_cnt = 1
        elif res_min == cnt:
            res_cnt += 1
    else:
        if n*2 <= b:
            dfs(n*2, cnt+1)
        if n+1 <= b and vistied[n+1] == 0:
            if n+1 != b:
                vistied[n+1] = 1
            dfs(n+1, cnt+1)
        if n-1 >= 0 and vistied[n-1] == 0:
            if n-1 != b:
                vistied[n-1] = 1
            dfs(n-1, cnt+1)
        
dfs(a, 0)

print(res_min)
print(res_cnt)