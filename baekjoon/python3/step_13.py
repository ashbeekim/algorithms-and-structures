# -*- coding: utf-8 -*-
# geometry 1
import sys
import math


# 1085
x, y, w, h = map(int, input().split())
lst = [x, y, w-x, h-y]
print(min(lst))


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


# 2477


# 3053
def ucl_circle(r):
    return math.pi*(r**2)


def txc_circle(r):
    return 2*(r**2)


r = int(input())
print(ucl_circle(r))
print(txc_circle(r))


# 1002


# 1004


# 1358
