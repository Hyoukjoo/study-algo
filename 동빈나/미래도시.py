import collections
import heapq
import sys

n, m = 5, 7
x, k = 4, 5

exam = [[1,2], [1,3], [1,4], [2,4], [3,4], [3,5], [4,5]]

table = [[sys.maxsize] * n for _ in range(n)]

for x, y in exam:
    x -= 1
    y -= 1
    table[x][y] = 1
    table[y][x] = 1
    
for i in range(n):
    table[i][i] = 0
    
for c in range(n):
    for a in range(n):
        for b in range(n):
            table[a][b] = min(table[a][b], table[a][c] + table[c][b])
        
distance = table[1][k-1] + table[k-1][x-1]

print(distance)