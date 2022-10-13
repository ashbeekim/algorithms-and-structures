# -*- coding: utf-8 -*-
# cumulative sum
import sys


input = sys.stdin.readline


# 11659
n, m = map(int, input().split())
n_lst = list(map(int, input().split()))
prefix_sum = [0]
tmp = 0

for i in n_lst:
    tmp += i
    prefix_sum.append(tmp)
 
for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])


# 2559


# 16139


# 10986


# 11660

"""
11658, 되게 쉬운 방법으로 풀이하니가 시간 초과.
        위의 방식으로 풀이는 했으나, accuumulate한 부분의 코드를 간결하게 할 방법을 고려할 필요가 있음.
"""
