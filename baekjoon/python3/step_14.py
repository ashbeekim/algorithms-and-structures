# -*- coding: utf-8 -*-
# number theory & combinatorics
import sys
import math
from itertools import combinations


# 5086


# 1037
n = int(input())
nums = list(map(int, input().split()))
print(min(nums)*max(nums))


# 2609
a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))


# 1934
n = int(input())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))


# 2981


# 3036


# 11050
n, k = map(int, sys.stdin.readline().split())

print(len(list(combinations(range(n), k))))


# 11051


# 1010


# 9375


# 1676


# 2004


"""
"""
