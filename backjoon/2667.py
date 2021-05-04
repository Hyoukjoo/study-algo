n = int(input())

house = [list(map(int, list(input()))) for _ in range(n)]

result = []
cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x > n - 1 or y > n - 1: return
    if house[x][y] != 0:
        house[x][y] = 0
        cnt += 1
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
for i in range(n):
    for j in range(n):
        if house[i][j] != 0:
            dfs(i, j)
            result.append(cnt)
            cnt = 0
           
print(len(result)) 
for answer in sorted(result):
    print(answer)
            
            