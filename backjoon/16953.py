import sys
from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])
answer = sys.maxsize

while q:
    num, cnt = q.popleft()
    
    if num == b:
        answer = min(answer, cnt)
    if num * 2 <= b:
        q.append((num*2, cnt+1))
    if int(str(num) + '1') <= b:
        q.append((int(str(num) + '1'), cnt+1))

print(-1 if answer == sys.maxsize else answer)