import sys
import math


# 1978

# 2581

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
