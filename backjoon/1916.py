import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

table = defaultdict(list)
dist = defaultdict(int)

for _ in range(m):
    start, end, cost = tuple(map(int, input().split()))
    table[start].append((cost, end)) 

s, e = map(int, input().split())
heap = [(0, s)]

while heap:
    time, node = heapq.heappop(heap)
    if not node in dist:
        dist[node] = time
        for cost, end in table[node]:
            alt = time + cost
            heapq.heappush(heap, (alt, end))
            
print(dist[e])