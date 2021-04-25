def solution(numbers, target):
    cnt = 0
    
    def dfs(_sum, idx):
        if idx == len(numbers) and _sum == target:
            cnt += 1
        if idx < len(numbers):
            dfs(_sum + numbers[idx], idx+1)
            dfs(_sum - numbers[idx], idx+1)
            
    dfs(0, 0)
    return cnt