h, m = map(int, input().split())

time = h * 60 + m - 45

if time < 0:
    time = 1440 + time

nh = time // 60
nm = time % 60

print(nh, nm)

