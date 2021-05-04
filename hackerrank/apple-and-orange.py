s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())

apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

apple_num = 0
orange_num = 0

for i in range(max(m ,n)):
    if i < m:
        d = apples[i] + a
        if d >= s and d <= t:
            apple_num += 1
    if i < n:
        d = oranges[i] + b
        if d >= s and d <= t:
            orange_num += 1

print(apple_num)
print(orange_num)

