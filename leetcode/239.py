class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        
        for i, n in enumerate(nums):
            while window and nums[window[-1]] <= n:
                window.pop()
            
            window.append(i)
            
            if i - window[0] >= k:
                window.popleft()
                
            if i + 1 >= k:
                result.append(nums[window[0]])
                
        return result