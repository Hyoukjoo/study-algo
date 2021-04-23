import sys
input = sys.stdin.readline

yoots = [input().split() for _ in range(3)]

result = []

for i in range(3):
    c = yoots[i].count('0')

    if c == 0:
        result.append('E')
    elif c == 1:
        result.append('A')
    elif c == 2:
        result.append('B')
    elif c == 3:
        result.append('C')
    elif c == 4:
        result.append('D')

for a in result:
    print(a)
    
