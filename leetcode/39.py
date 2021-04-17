class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, start, path):
            if csum > target:
                return
            if csum == target:
                result.append(path)
                return
            
            for i in range(start, len(candidates)):
                dfs(csum + candidates[i], i, path + [candidates[i]])
                
        dfs(0, 0, [])
        
        return result