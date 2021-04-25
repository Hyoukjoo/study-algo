import itertools 

def solution(numbers):
    result = 0
    lst = list(numbers)
    nums = set()

    for i in range(len(numbers)):
        p = list(itertools.permutations(lst, i + 1))
        s = set(p)
        while s:
            n = int(''.join(list(s.pop())))
            nums.add(n)

    for n in nums:
        if is_prime(n):
            result += 1
    
    return result


def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
