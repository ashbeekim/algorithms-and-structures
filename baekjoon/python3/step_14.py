# -*- coding: utf-8 -*-
# number theory & combinatorics
import sys
import math
from itertools import combinations


input = sys.stdin.readline


# 5086
while True:
    a, b = map(int, input().split())
    if (a==0)&(b==0):
        break
    if b%a==0:
        print('factor')
    elif a%b==0:
        print('multiple')
    else:
        print('neither')


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
    a, b = map(int, input().split())
    print(math.lcm(a, b))


# 2981


# 3036
def calc_gcd(lg_num, sm_num):
    while sm_num!=0:
        mod = lg_num%sm_num
        lg_num = sm_num
        sm_num = mod
    return lg_num


n = int(input())
lst = list(map(int, input().split()))
benchmark = lst.pop(0)

for _ in range(n-1):
    _gcd = calc_gcd(benchmark, lst[_])
    print('{}/{}'.format(benchmark//_gcd, lst[_]//_gcd))


# 11050
n, k = map(int, input().split())

print(math.comb(n, k))


# 11051
n, k = map(int, input().split())

print(math.comb(n, k)%10007)


# 1010
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(math.factorial(m) // (math.factorial(n)*math.factorial(m-n)))


# 9375


# 1676
n = int(input())
cnt = 0
for x in str(math.factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)


# 2004


"""
# 3036, 기약분수: 분모와 분자가 1 외에는 공약수가 없는 분수
    기약분수는 분모, 분자가 서로소. 즉, 최대공약수가 1이란 말과 같음.
    따라서 두 수의 최대공약수로 나누면 기약분수가 됨.
# 11050, 
    itertools.combinations로 풀면, 메모리는 줄어드는데 시간이 조금 더 걸리고,
    math.comb로 풀면, 메모리는 조금 늘어나는 대신, 연산 시간이 줄어듦.
# 1010, mCn, m!/(n!*(m-n)!)
"""
