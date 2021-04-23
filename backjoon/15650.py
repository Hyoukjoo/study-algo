import sys, itertools
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [str(i + 1) for i in range(n)]

for num in list(itertools.combinations(nums, m)):
    print(' '.join(num))

