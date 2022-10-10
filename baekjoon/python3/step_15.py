# -*- coding: utf-8 -*-
# backtracking
import sys
import itertools


input = sys.stdin.readline


# 15649
n, m = map(int, input().split())
data = list(itertools.permutations(range(1, n+1), m))

for _ in data:
    print(' '.join(list(map(str, _))))


# 15650
n, m = map(int, input().split())
data = list(itertools.combinations(range(1, n+1), m))

for _ in data:
    print(' '.join(list(map(str, _))))

# 15651
n, m = map(int, input().split())
tmp = list(range(1, n+1))   # 한 번에 다 선언하고, for로 돌리면 메모리 약 4배, 시간 1.1배

for _ in itertools.product(tmp, repeat=m):
    print(' '.join(map(str, _)))


# 15652
n, m = map(int, input().split())
tmp = list(range(1, n+1))

for _ in itertools.combinations_with_replacement(tmp, m):
    print(' '.join(map(str, _)))


# 9663


# 2580


# 14888


# 14889


"""
"""
