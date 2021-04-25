import math

def solution(answers):
    n = len(answers)
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    result = []
    
    for i, v in enumerate(answers):
        if v == a[i % len(a)]:
            score[0] += 1
        if v == b[i % len(b)]:
            score[1] += 1
        if v == c[i % len(c)]:
            score[2] += 1


    for i, v in enumerate(score):
        if v == max(score):
            result.append(i+1)
    
    return result

arg = [1,2,3,4,5]
print(solution(arg))