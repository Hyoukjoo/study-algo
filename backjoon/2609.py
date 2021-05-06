n1, n2 = map(int, input().split())

def solution(a, b):
    if b == 0:
        print(a)
        print(n1 * n2 // a)
    else:
        return solution(b, a % b)
    
solution(n1, n2)