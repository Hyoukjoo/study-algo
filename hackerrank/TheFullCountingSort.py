#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    n = len(arr)
    result = [''] * n
    for i in range(n):
        if i < n // 2:
            arr[i][1] = '-'
            
        result[int(arr[i][0])] += arr[i][1] + ' '
        
    print(''.join(result))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
