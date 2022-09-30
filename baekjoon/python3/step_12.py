# -*- coding: utf-8 -*-
# set & map
import sys


# 10815
n = int(input())
n_lst = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_lst = list(map(int, sys.stdin.readline().split()))

_dict = {}
for _ in range(n):
    _dict[n_lst[_]] = 0

res = ''
for _ in range(m):
    if m_lst[_] in _dict:
        res += '1 '
    else:
        res += '0 '
print(res)


# 14425


# 1620


# 10816
n = int(input())
n_lst = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_lst = list(map(int, sys.stdin.readline().split()))

_dict = {}
for _ in range(n):
    if n_lst[_] not in _dict:
        _dict[n_lst[_]] = 1
    else:
        _dict[n_lst[_]] += 1

for _ in range(m):
    if m_lst[_] in _dict:
        print(_dict[m_lst[_]], end=' ')
    else:
        print(0, end=' ')


# 1764


# 1269
n = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
comp = set(A + B)
print((len(comp) - len(A)) + (len(comp) - len(B)))


# 11478


"""
# 10815, 10816, dict 형식으로 선언하지 않으면, 시간 초과 발생
# 1269, 람다식으로 선언해서 하니까 오히려 이번 문제에선 시간 초과가 문제가 되었음.
    차집합 구하는 방식으로 문제를 해결함.
"""
