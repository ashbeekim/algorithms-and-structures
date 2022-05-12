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

# 4948

# 9020

# 1085

# 3009

# 4153
while True:
    nums = list(map(int, sys.stdin.readline().strip().split()))
    if (nums[0] == 0)&(nums[1] == 0)&(nums[2] == 0):
        break
    else:
        c = max(nums)
        a, b = list(filter(lambda x: x != c, nums))
        if (a ** 2) + (b ** 2) == (c ** 2):
            print("right")
        else:
            print("wrong")

# 3053

# 1002

"""
# 1978, 2581은 동일하게 소수를 찾는 함수를 사용하기에 코드 중복 방지 차원에서 상단에 작성함.
    처음에 분명 소수를 구하는 값이라고 생각하고 작성했었는데, 1에 대한 예외처리를 하지 않아서 틀렸었음.
"""
