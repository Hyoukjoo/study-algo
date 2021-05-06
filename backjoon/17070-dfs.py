import sys
input = sys.stdin.readline

n = int(input())

wall = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def dfs(x, y, d):
    global cnt
    if x == n - 1 and y == n - 1: cnt += 1
    if d == 0:
        if y+1 < n and wall[x][y+1] == 0: dfs(x, y+1, 0)
        if x+1 < n and y+1 < n:
            if wall[x+1][y+1] == 0 and wall[x][y+1] == 0 and wall[x+1][y] == 0: 
                dfs(x+1, y+1, 2)
    elif d == 1:
        if x+1 < n and wall[x+1][y] == 0: dfs(x+1, y, 1)
        if x+1 < n and y+1 < n:
            if wall[x+1][y+1] == 0 and wall[x][y+1] == 0 and wall[x+1][y] == 0: 
                dfs(x+1, y+1, 2)
    elif d == 2:
        if y+1 < n and wall[x][y+1] == 0: dfs(x, y+1, 0)
        if x+1 < n and wall[x+1][y] == 0: dfs(x+1, y, 1)
        if x+1 < n and y+1 < n:
            if wall[x+1][y+1] == 0 and wall[x][y+1] == 0 and wall[x+1][y] == 0: 
                dfs(x+1, y+1, 2)
                
dfs(0, 1, 0)

print(cnt)
