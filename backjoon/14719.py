h, w = map(int, input().split())

wall = list(map(int, input().split()))

stack = []

p = 0
water = 0

for p in range(w):
    while stack and wall[stack[-1]] < wall[p]:
        prev = stack.pop()

        if not stack: break

        height = min(wall[p], wall[stack[-1]]) - wall[prev]
        distance = p - stack[-1] - 1

        water += distance * height
        
    stack.append(p)

print(water)