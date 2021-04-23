import sys, itertools
from collections import deque

input = sys.stdin.readline

n = int(input())

commands = [input().split() for _ in range(n)]

dq = deque([])

for command in commands:
    c = command[0]
    if c == 'push_back':
        dq.append(command[1])
    elif c == 'push_front':
        dq.appendleft(command[1])
    elif c == 'pop_front':
        if dq:
            print(dq.popleft())
        else: 
            print(-1)
    elif c == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif c == 'size':
        print(len(dq))
    elif c == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if dq:
            print(dq[0])
        else: 
            print(-1)
    elif c == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)