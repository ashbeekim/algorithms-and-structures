# !/bin/python3

import os
import sys
import re, math, random
from collections import Counter


# Sales by Match
def sockMerchant(n, ar):
    # Write your code here
    dt = Counter(ar)
    return sum(list(map(lambda x: x[1] // 2, dt.items())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


# Zig Zag Sequence
'''
debug rule
    * modify at most three lines
    * cannot add or remove lines of code
constraints
    * n is always odd
case 1
    a = [2, 3, 5, 1, 4], n = 5
    return [1, 4, 5, 3, 2]
case 2
    a = [1 ,2 ,3 ,4 ,5 ,6 ,7], n = 7
    return [1 ,2 ,3 ,7 ,6 ,5 ,4]
'''
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]
    st = mid + 1
    ed = n - 2

    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
    
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


# Drawing Book


# Tower Breakers


# Caesar Cipher


# Max Min


# Dynamic Array


# Grid Challenge


# Prime Dates


# Sherlock and Array


# Recursive Digit Sum


# Counter game


# Sum vs XOR


