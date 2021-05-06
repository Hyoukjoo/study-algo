n = int(input())

for num in list(map(int, input().split())):
    if num == 1:
        n -= 1
        continue

    i = 2
    while i * i <= num:
        if num % i == 0: 
            n -= 1
            break
        i += 1

print(n)