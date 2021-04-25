def solution(n, computers):
    answer = 0
    
    def dfs(y):
        for i in range(n):
            if computers[y][i] == 1:
                computers[y][i] = 0
                if y != i:
                    computers[i][y] = 0
                    dfs(i)
                
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                answer += 1
                dfs(j)
                
    return answer