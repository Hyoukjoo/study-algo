a,b = [int(input()) for _ in range(2)]

print(a * (b % 10))
print((a * ((b // 10)%10)))
print(a * (b // 100))
print(a*b)