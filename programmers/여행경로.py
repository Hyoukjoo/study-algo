from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for key, value in sorted(tickets, reverse=True):
        graph[key].append(value)

    route = []

    def dfs(f):
        while graph[f]:
            dfs(graph[f].pop())
        route.append(f)

    dfs('ICN')

    return route

arg = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(arg)