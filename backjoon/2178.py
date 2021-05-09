import sys
from collections import deque

n, m = map(int, input().split())

maze = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
    
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
q = deque([(0, 0)])
visited[0][0] = 1
    
while q:
    y, x = q.popleft()
    
    if [y, x] == [n-1, m-1]: 
        print(visited[y][x])
        break
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == '1' and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))