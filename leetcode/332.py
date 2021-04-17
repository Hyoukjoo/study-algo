class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        graph = collections.defaultdict(list)
        
        for key, value in sorted(tickets, reverse=True):
            graph[key].append(value)
            
        result = []
        
        def dfs(f):
            while graph[f]:
                dfs(graph[f].pop())
            result.append(f)
            
        dfs('JFK')
        
        return result[::-1]
            
        
        