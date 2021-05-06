import sys
input = sys.stdin.readline

n = int(input())

wall = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n] * n

dp[0] = [0,0] + [1] * (n - 2)
dp[1] = [0,0] + [1] * (n - 2)

for i in range(0, n):
    for j in range(3, n):
        if wall[i][j] == 1:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i][j-1]
        
print(dp)