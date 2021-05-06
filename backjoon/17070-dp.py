import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

if maps[-1][-1] == 1: 
    print(0)
    sys.exit()

dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(2, n):
    if maps[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]
        
for r in range(1, n):
    for c in range(2, n):
        if maps[r][c] == maps[r][c-1] == maps[r-1][c] == 0:
            dp[r][c][2] = sum(dp[r-1][c-1])
        if maps[r][c] == 0:
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
            
print(sum(dp[-1][-1]))