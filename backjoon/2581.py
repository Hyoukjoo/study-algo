import sys

input = sys.stdin.readline
print = sys.stdin.write

m = int(input())
n = int(input())

arr = []

def check_prime(num):
    if num == 1: 
        return False
    if num == 2 or num == 3:
        return True

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

for i in range(m, n + 1):
    if check_prime(i):
        arr.append(i)
    
if not arr:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
    