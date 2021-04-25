import sys

def solution(begin, target, words):
    if not target in words: return 0
    
    answer = sys.maxsize
    
    def dfs(s, visited):
        nonlocal answer
        if s == target: 
            answer = min(answer, len(visited))
        else:
            for i in range(len(words)):
                if not i in visited:
                    if compare(s, words[i]):
                        dfs(words[i], visited + [i])
    dfs(begin, [])
    
    return answer

def compare(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    return True if cnt == len(a) - 1 else False