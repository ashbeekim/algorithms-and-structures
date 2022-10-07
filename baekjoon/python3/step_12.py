# -*- coding: utf-8 -*-
# set & map
from curses.ascii import isdigit
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
n, m = map(int, input().split())
n_set = set()
cnt = 0

for _ in range(n):
    n_set.add(sys.stdin.readline().strip())

for _ in range(m):
    if sys.stdin.readline().strip() in n_set:
        cnt += 1

print(cnt)


# 1620
n, k = map(int, input().split())
int_dict = {}
str_dict = {}

for _ in range(n):
    name = sys.stdin.readline().strip()
    int_dict[_] = name
    str_dict[name] = _

for _ in range(k):
    q = sys.stdin.readline().strip()
    if q.isdigit()==True:
        print(int_dict[int(q)-1])
    else:
        print(str_dict[q] + 1)


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
