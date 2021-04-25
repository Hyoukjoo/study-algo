import collections
from functools import reduce

def solution(clothes):
    answer = 1
    dic = collections.Counter([kind for wear, kind in clothes])

    return reduce(lambda x, y: x*(y+1), dic.values(), 1) -1