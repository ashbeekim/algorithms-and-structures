# -*- coding: utf-8 -*-
# sort
import sys


# 2750


# 2751


# 10989


# 2108


# 1427


# 11650


# 11651


# 1181
N = int(sys.stdin.readline())
arr = list(set([sys.stdin.readline().strip() for _ in range(N)]))
arr.sort(key = lambda x: (len(x), x))
print('\n'.join(arr))


# 10814


"""

"""
