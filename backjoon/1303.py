from collections import defaultdict
from functools import reduce

n, m = map(int, input().split())

sols = [input() for _ in range(m)]

checked = [[False] * n for _ in range(m)]

count = defaultdict(int)
res = defaultdict(list)

def bfs(x, y, sol):
    if checked[x][y] == True or sols[x][y] != sol:
        return
    
    count[sol] += 1
    checked[x][y] = True
    
    if x - 1 >= 0: bfs(x-1, y, sol)
    if y - 1 >= 0: bfs(x, y-1, sol)
    if x + 1 < n: bfs(x + 1, y, sol)
    if y + 1 < m: bfs(x, y+1, sol)

for i in range(n):
    for j in range(m):
        sol = sols[i][j]
        bfs(i, j, sol)
        if count[sol] != 0:
            res[sol].append(count[sol])
            count[sol] = 0
        
ans = []
for values in res.values():
    _sum = reduce(lambda acc, cur: acc + cur ** 2, values, 0)
    ans.append(str(_sum))
    
print(' '.join(ans))