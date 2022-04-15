# -*- coding: utf-8 -*-
# math1
# 1712
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)
    
# 2292

# 1193

# 2869

# 10250

# 2775

# 2839

# 10757

def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)
def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
