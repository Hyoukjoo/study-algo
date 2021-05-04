n = int(input())
candies = [list(input()) for _ in range(n)]
longest = 0

def check(s_row, e_row, s_col, e_col):
    global longest
    
    for i in range(s_row, e_row + 1):
        cnt = 1
        for j in range(1, n):
            if candies[i][j] == candies[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)
        
    for i in range(s_col, e_col + 1):
        cnt = 1
        for j in range(1, n):
            if candies[j][i] == candies[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)

check(0, n - 1, 0, n - 1)

for i in range(n - 1):
    for j in range(n - 1):
        candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        check(i, i, j, j + 1)
        candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
        check(i, i + 1, j, j)
        candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

print(longest)