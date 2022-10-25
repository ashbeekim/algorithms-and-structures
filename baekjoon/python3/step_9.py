# -*- coding: utf-8 -*-
# sort
import sys
from statistics import mean, median
from collections import Counter
from operator import itemgetter


input = sys.stdin.readline

# 2750
t = int(input())
arr = []

for _ in range(t):
    arr.append(int(input()))
arr.sort()

for _ in range(len(arr)):
    print(arr[_])


# 2587
arr = []

for _ in range(5):
    arr.append(int(input()))

print(int(mean(arr)))
print(int(median(arr)))


# 25305
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr[k-1])


# 2751
t = int(input())
arr = []

for _ in range(t):
    arr.append(int(input()))
arr.sort()

for _ in range(len(arr)):
    print(arr[_])


# 10989
n = int(input())
arr = [0] * 10001

for _ in range(n):
    num = int(input())
    arr[num] += 1

for i in range(10001):
    if arr[i]!=0:
        for _ in range(arr[i]):
            print(i)


# 2108
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

if len(arr)==1:
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(0)
else:
    print(int(round(sum(arr)/N)))
    print(arr[int(N/2)])
    c_arr = sorted(Counter(arr).items(), key=lambda x: (-x[1], x[0]))
    cnt = c_arr[0][1]
    c_arr = list(filter(lambda x: x[1]==cnt, c_arr))
    if len(c_arr)==1:
        print(c_arr[0][0])
    else:
        print(c_arr[1][0])
    print(arr[-1] - arr[0])


# 1427
n = list(input().strip())
n.sort(reverse=True)
print(''.join(n))


# 11650
n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))
arr = sorted(arr, key=lambda x: (x[0], x[1]))

for _ in arr:
    print(_[0], _[1])


# 11651
n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))
arr = sorted(arr, key=lambda x: (x[1], x[0]))

for _ in arr:
    print(_[0], _[1])


# 1181
N = int(input())
arr = list(set([input().strip() for _ in range(N)]))
arr.sort(key = lambda x: (len(x), x))
print('\n'.join(arr))


# 10814
def multisort_by_idx(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs

n = int(input())
arr = []

for _ in range(n):
    num, word = input().split()
    arr.append((int(num), word.strip(), _))
arr = multisort_by_idx(arr, ((0, False), (2, False)))

for _ in arr:
    print(_[0], _[1])


# 18870
n = int(input())
arr = list(map(int, input().split()))
tmp = dict([(_v, idx) for idx, _v in enumerate(sorted(list(set(arr))))])

for _ in arr:
    print(tmp[_], end=' ')


"""
# 10989, 정렬할 값의 할당 없이 작성 시 메모리 초과 발생
    정렬된 수의 최댓값은 10000까지 가능하기 때문에 파이썬의 인덱스를 고려하면 10001개의 공간 할당.
# 2108, 최빈값 중복 시 처리 규칙에서 약간 고민했던 문제.
# 10814, 메모리(55468 KB -> 48536 KB), 시간(336 ms -> 324 ms)
    파이썬 공식 문서 중 정렬 참고하니까 메모리 및 시간 효율이 좋아짐.
# 18870, 값에 따라 순서 적용. set없이 진행하면 시간 초과 발생.
"""
