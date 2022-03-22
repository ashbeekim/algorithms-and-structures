#!/bin/python3

import math
import os
import random
import re
import sys

# Plus Minus
def plusMinus(arr):
    # Write your code here
    plus = list(filter(lambda x: x>0, arr))
    minus = list(filter(lambda x: x<0, arr))
    zero = list(filter(lambda x: x==0, arr))
    print(len(plus)/len(arr))
    print(len(minus)/len(arr))
    print(len(zero)/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# Mini-Max Sum
def miniMaxSum(arr):
    # Write your code here
    sums = []
    for i in range(len(arr)):
    #     sums.append(sum(list(filter(lambda x: x!=arr[i], arr)))) ## 한 케이스에서 Wrong Answer 발생 >> drop
        left = [] if i==0 else arr[:i]
        right = [] if i==len(arr)-1 else arr[i+1:]
        sums.append(sum(left + right))

    print(min(sums), max(sums), sep=" ")
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# Time Conversion
def timeConversion(s):
    # Write your code here
    s, comp = s[:-2], s[-2:]
    times = list(map(str, s.split(':')))
    if (comp=="AM")&(times[0]=="12"):
        return ":".join(["00", times[1], times[2]])
    elif ((comp=="PM")&(times[0]=="12"))|(comp=="AM"):
        return ":".join(times)
    else:
        return ":".join([str(int(times[0])+12), times[1], times[2]])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


# Sparse Arrays
def matchingStrings(strings, queries):
    # Write your code here
    result = []
    for _ in queries:
        result.append(strings.count(_))
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()


# Lonely Integer


# Flipping bits


# Diagonal Difference


# Counting Sort 1


# Pangrams


# Permuting Two Arrays


# Subarray Division 1


# XOR Strings 2


# Mock Test

