s = int(input())

i = 1
_sum = 0

while True:
    _sum += i
    if _sum > s:
        print(i - 1)
        break
    elif _sum == s:
        print(i)
        break
    else:
        i += 1