import sys, itertools
from collections import deque

input = sys.stdin.readline

nums = deque([i + 1 for i in range(int(input()))])

while len(nums) > 1:
    nums.popleft()
    nums.rotate(-1)

print(nums.pop())

