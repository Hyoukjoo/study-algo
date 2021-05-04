from itertools import permutations

n, k = map(int, input().split())

if k < 5:
    print(0)
else:
    words = permutations([input() for _ in range(n)])
    ans = 0
    for permu in words:
        s = set()
        cnt = 0
        for word in permu:
            s.update(word)
            if len(s) <= k:
                cnt += 1
        ans = max(cnt, ans)

    print(ans)