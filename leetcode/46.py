class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        arr = []
        size = len(nums)
        
        def dfs():
            if len(arr) == size:
                result.append(arr[:])
            else:
                for v in nums:
                    if v not in arr:
                        arr.append(v)
                        dfs()
                        arr.pop()
                
        dfs()
        
        return result