class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                that = stack.pop()
                result[that] = i - that
            
            stack.append(i)
            
        return result
    