# -*- coding: utf-8 -*-
# set & map
import sys


# 10815


# 14425


# 1620


# 10816


# 1764


# 1269
n = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
comp = set(A + B)
print((len(comp) - len(A)) + (len(comp) - len(B)))


# 11478


"""
# 1269, 람다식으로 선언해서 하니까 오히려 이번 문제에선 시간 초과가 문제가 되었음.
    차집합 구하는 방식으로 문제를 해결함.
"""
