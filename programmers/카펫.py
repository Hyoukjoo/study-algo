def solution(brown, yellow):
    _sum = brown + yellow
    multi_num = []

    for i in range(_sum, 2, -1):
        if _sum % i == 0:
            j = _sum // i
            if yellow == (i-2) * (j-2):
                return [i, j]

print(solution(12,4))