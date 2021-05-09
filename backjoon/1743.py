import collections

n, m, k = map(int, input().split())

trash = [tuple(map(int, input().split())) for _ in range(k)]
ground = [[0] * m for _ in range(n)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0

for i, j in trash:
    ground[i-1][j-1] = 1

def bfs(t):
    global ground
    cnt = 0
    q = collections.deque([t])
    
    while q:
        cnt += 1
        y, x = q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and ground[ny][nx] == 1:
                ground[ny][nx] = 0
                q.append((ny, nx))
               
    return cnt
        
for i in range(n):
    for j in range(m):
        if ground[i][j] == 1:
            ground[i][j] = 0
            answer = max(answer, bfs((i, j)))
        
print(answer)