class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if grid[x][y] == '0': return 
            
            grid[x][y] = '0'
            
            if x - 1 >= 0: dfs(x - 1, y)
            if y - 1 >= 0: dfs(x, y - 1)
            if x + 1 < len(grid): dfs(x + 1, y)
            if y + 1 < len(grid[x]): dfs(x, y + 1)
            
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
                    
        return ans