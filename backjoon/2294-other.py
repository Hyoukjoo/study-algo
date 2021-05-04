n, k = map(int, input().split())

coins = sorted([int(input()) for _ in range(n)])

dp = [10001] * 10001
dp[0] = 0

for i in range(1, k + 1):
    for coin in coins:
        if coin > i: break
        dp[i] = min(dp[i - coin] + 1, dp[i])
        
print(dp[k] if dp[k] != 10001 else -1)