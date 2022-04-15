# -*- coding: utf-8 -*-
# for
'''
input으로만 처리하니까 RuntimeError나는 경우가 발생해서 내장 라이브러리 호출함
'''
import sys


# 2739
n = int(input())
assert (n>0)&(n<10)
for i in range(1, 10, 1):
    print(f'{n} * {i} = {n*i}')

# 10950
n = int(sys.stdin.readline())
for i in range(1, n+1, 1):
    a, b = map(int, sys.stdin.readline().split())
    assert (a > 0)&(a < 10)&(b > 0)&(b < 10)
    print(a+b)

# 8393
n = int(input())
if n%2 == 0:
    print((1+n)*(n//2))
else:
    print(((1+n)*(n//2+1))-(n//2+1))
    
# 15552
n = int(sys.stdin.readline())
for i in range(1, n+1, 1):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

# 2741
n = int(input())
assert (n>0)&(n<=100000)
for i in range(n):
    print(i+1)

# 2742
n = int(input())
for i in sorted(range(n),reverse=True):
    print(i+1)

# 11021
n = int(sys.stdin.readline())
for i in range(1, n+1, 1):
    a, b = map(int, sys.stdin.readline().split())
    assert (a > 0)&(a < 10)&(b > 0)&(b < 10)
    print(f'Case #{i}: {a+b}')

# 11022
n = int(sys.stdin.readline())
for i in range(1, n+1, 1):
    a, b = map(int, sys.stdin.readline().split())
    assert (a > 0)&(a < 10)&(b > 0)&(b < 10)
    print(f'Case #{i}: {a} + {b} = {a + b}')

# 2438
n = int(input())
assert (n>=1)&(n<=100)
for i in range(1, n+1, 1):
    print("*"*i)

# 2439
n = int(input())
assert (n>=1)&(n<=100)
for i in range(1, n+1, 1):
    print(" "*(n-i)+"*"*i)
    
# 10871
N, X = map(int, sys.stdin.readline().split())
assert (N>=1)&(N<=10000)&(X>=1)&(X<=10000)
A = list(map(int, sys.stdin.readline().split()))
B = []
for i in A:
    assert (i>=1)&(i<=10000)
    if i<X:
        B.append(str(i))
print(" ".join(B))

# 10952
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        assert (a>0)&(a<10)&(b>0)&(b<10)
        print(a+b)
    except:
        break

# 10951
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        assert (a>0)&(a<10)&(b>0)&(b<10)
        print(a+b)
    except:
        break

# 1110
N = arr = input()
cnt = 0
while True:
    if (cnt > 0)&(int(N)==int(arr[-2:])):
        print(cnt)
        break
    arr = arr if int(arr) >= 10 else "0" + arr
    num = int(arr[-2]) + int(arr[-1]) if int(arr[-2]) + int(arr[-1]) < 10 else int(arr[-2]) + int(arr[-1]) - 10
    arr = arr + str(num)
    cnt += 1
