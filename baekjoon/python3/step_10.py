# -*- coding: utf-8 -*-
# brute-force
import sys
from itertools import combinations

# 2798
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum_arr = []
for _ in combinations(arr, 3):
    sum_arr.append(sum(_))
sum_arr = list(filter(lambda x: x <= M, sum_arr))
print(max(sum_arr))


# 2231


# 7568


# 1018


# 1436

