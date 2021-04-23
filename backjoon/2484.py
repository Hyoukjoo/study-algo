import sys
input = sys.stdin.readline

def money():
    lst = sorted(list(map(int, input().split())))

    if len(set(lst)) == 1:
        return 50000 + lst[0] * 5000
    elif len(set(lst)) == 2:
        return 10000 + lst[1] * 1000 if lst[1] == lst[2] else 2000 + (lst[1] + lst[2]) * 500
    for i in range(3):
        if lst[i] == lst[i+1]: 
            return 1000 + lst[i] * 100
    return lst[-1] * 100

print(max(money() for _ in range(int(input()))))

# n = int(input())

# dices = [list(map(int, input().split())) for _ in range(n)]

# result = -sys.maxsize

# def getMoney(dice):
#     _sum = 0
#     arr = [0] * 6
#     for num in dice:
#         arr[num - 1] += 1
    
#     for i in range(6):
#         if arr[i] == 4:
#             _sum += 50000 + (i + 1) * 5000
#             break
#         elif arr[i] == 1 or arr[i] == 3:
#             if 3 in arr:
#                 target = arr.index(3)
#                 _sum += 10000 + (target + 1) * 1000
#                 break
#             elif arr.count(1) == 4:
#                 for j in range(5, -1, -1):
#                     if arr[j] == 1:
#                         _sum += (j + 1) * 100
#                         break
#                 break
#             elif arr.count(1) == 2:
#                 target = arr.index(2)
#                 _sum += 1000 + (target + 1) * 100
#                 break
#         elif arr[i] == 2:
#             if arr.count(2) == 2:
#                 one, two = list(filter(lambda x: arr[x] == 2, range(6)))
#                 _sum += 2000 + (one + 1) * 500 + (two + 1) * 500
#                 break
#             else:
#                 _sum += 1000 + (i + 1) * 100
#                 break

#     return _sum

# for dice in dices:
#     result = max(result, getMoney(dice))

# print(result)