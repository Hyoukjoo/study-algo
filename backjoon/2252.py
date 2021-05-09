import collections

n, m = map(int, input().split())

students = [list(map(int, input().split())) for _ in range(m)]

q = collections.deque()
graph = collections.defaultdict(list)

degree = [0] * (n+1)

for a, b in students:
    degree[b] += 1
    graph[a].append(b)

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    student = q.popleft()
    for target in graph[student]:
        degree[target] -= 1
        if degree[target] == 0:
            q.append(target)
    print(student, end=' ')