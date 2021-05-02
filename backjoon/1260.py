from collections import defaultdict, deque

n, m, v = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

graph = defaultdict(list)

for s, e in sorted(edges):
    graph[s].append(e)
    graph[e].append(s)
    
def dfs(graph, v):
    visited = []
    stack = [v]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(reversed(graph[n]))
        
    return visited

def bfs(graph, v):
    visited = []
    queue = deque([v])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
        
    return visited
    

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))