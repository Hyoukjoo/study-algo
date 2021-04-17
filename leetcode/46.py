class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_el = []
        
        def dfs(el):
            if len(el) == 0:
                result.append(prev_el[:])
            
            for e in el:
                next_el = el[:]
                next_el.remove(e)
                
                prev_el.append(e)
                dfs(next_el)
                prev_el.pop()
        
        dfs(nums)
        
        return result
        
            