# _Arrays - DS

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.


def reverseArray(a):
    l = 0
    while l < len(a)/2:
        a[l], a[~l] = a[~l], a[l]
        l += 1
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
