class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        end = len(digits)
        
        def dfs(s, i):
            if i == end:
                result.append(s)
            else:
                for char in dic[digits[i]]:
                    dfs(s + char, i + 1)
        
        dfs('', 0)
        
        return [] if not digits else result
            
            