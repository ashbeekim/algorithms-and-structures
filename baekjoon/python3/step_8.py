import sys
import math


# 1978
def isprime(num):
    if num==1:
        return False
    else:
        for n in range(2, int(num**.5)+1):
            if num%n==0:
                return False
        return True
N = int(input())
arr = list(map(int, input().split()))
arr = list(map(isprime, arr))
arr = list(filter(lambda x: x==True, arr))
print(len(arr))


# 2581
a = int(input())
b = int(input())
arr = list(map(lambda x, y: (x, isprime(y)), range(a, b+1), range(a, b+1)))
arr = list(filter(lambda x: x[1]==True, arr))
if arr:
    arr = dict(arr)
    print(sum(arr.keys()))
    print(min(arr.keys()))
else:
    print(-1)


# 11653
def factorization(x): 
    d = 2 
    while d <= x: 
        if x % d == 0: 
            print(d) 
            x = x / d 
        else: 
            d = d + 1 
            
factorization(int(input()))


# 1929
## 앞서 사용한 isprime 활용
a, b = map(int, sys.stdin.readline().split())

for _ in range(a, b + 1):
    if isprime(_):
        print(_)


# 4948
prime_lst = [_ for _ in range(1, 123456 * 2 + 1) if isprime(_)]

while True:
    n = int(sys.stdin.readline())
    if n:
        lst = list(filter(lambda x: (x > n)&(x <= 2 * n), prime_lst))
        print(len(lst))
    else:
        break


# 9020

"""
# 1978, 2581은 동일하게 소수를 찾는 함수를 사용하기에 코드 중복 방지 차원에서 상단에 작성함.
    처음에 분명 소수를 구하는 값이라고 생각하고 작성했었는데, 1에 대한 예외처리를 하지 않아서 틀렸었음.
# 1929, 런타임에러를 자주 겪었는데, 몇 번 코드 수정하다가 sys를 사용하니까 풀렸음..
# 4948, 기존의 isprime 사용. 시간 초과 경우 방지를 위해 제한에 맞게 prime_lst 생성. lambda 식 조건 잘못 작성해서 몇 번의 에러를 겪었음.
"""
