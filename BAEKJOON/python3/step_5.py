# -*- coding: utf-8 -*-
# 1d array
import sys

# 10818
n = int(input())
arr = list(map(int, input().split()))
print(min(arr), max(arr), sep=' ')

# 2562
cnt, nums = 1, dict()
while cnt < 10:
    num = int(sys.stdin.readline())
    nums[num] = cnt
    cnt += 1
print(max(nums.keys()))
print(nums.get(max(nums.keys())))

# 2577

# 3052

# 1546

# 8958

# 4344
