import sys 
input = sys.stdin.readline

n = int(input())

coords = [list(map(int, input().split())) for _ in range(n)]

coords.sort(key=lambda x: (x[0], x[1]))

for coord in coords:
    print(' '.join(list(map(str, coord))))