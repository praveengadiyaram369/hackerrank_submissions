#!/bin/python3

import math
import os
import random
import re
import sys


def reverse_list(a, n, l, r):

    while l <= r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    a = reverse_list(a, n, 0, d-1)
    a = reverse_list(a, n, d, n-1)
    a = reverse_list(a, n, 0, n-1)

    for value in a:
        print(value, end=' ')
