n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

result = []

def dfs(arr, s):
    if sum(arr) == k:
        result.append(arr[:])
    elif sum(arr) < k:
        for i in range(s, n):
            arr.append(coins[i])
            dfs(arr, i)
            arr.pop()
            
dfs([], 0)

if not result:
    print(-1)
else:
    min_len = k + 1
    for a in result:
        min_len = min(min_len, len(a))
    print(min_len)
