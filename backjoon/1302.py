import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

books = [input().strip() for _ in range(n)]

books.sort()

c = Counter(books)

print(c.most_common(1)[0][0])