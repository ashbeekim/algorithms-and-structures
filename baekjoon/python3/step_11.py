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
N = int(input())

for _ in range(N + 1):
    res = _ + sum(map(int, str(_)))
    if res == N:
        print(_)
        break
else:
    print(0)


# 7568
N = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in arr:
    res = 1
    for j in arr:
        if (i[0] < j[0]) & (i[1] < j[1]):
            res += 1 
    print(res, end=' ')


# 1018


# 1436

