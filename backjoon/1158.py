import sys, itertools
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

people = deque([str(i + 1) for i in range(n)])

result = []

while people:
    people.rotate(-k + 1)
    result.append(people.popleft())

print('<' + ', '.join(result) + '>')
