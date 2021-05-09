import sys

n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = right = 0
_sum = 0
result = sys.maxsize

while right <= n:
    if _sum >= s:
        result = min(result, right - left)
        _sum -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        _sum += nums[right]
        right += 1
    # if _sum < s:
    #     _sum += nums[right]
    #     right += 1
    # else:
    #     _len = right - left
    #     if _len == 1: 
    #         print(1)
    #         exit()
    #     else:
    #         result = min(result, _len)
    #         _sum -= nums[left]
    #         left += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)