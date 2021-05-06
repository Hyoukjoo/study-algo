import sys
import collections
import itertools
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

if k < 5: 
    print(0)
else: 
    basic = set(list('acint'))
    new = set()

    words = []
    dic = collections.defaultdict(int)

    for _ in range(n):
        word = set(list(input().rstrip())) - basic
        
        if len(word) > k - 5: continue
        
        new |= word 
        
        words.append(word)
        
    new = map(set, itertools.combinations(new, k - 5))
        
    result = 0

    for s in new:
        cnt = 0
        for word in words:
            if word.issubset(s):
                cnt += 1
        result = max(result, cnt)
        
    print(result)