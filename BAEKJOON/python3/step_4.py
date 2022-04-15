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
a = int(input())
b = int(input())
c = int(input())
n_bucket = {i:0 for i in range(10)}
num = list(map(int, list(str(a*b*c))))
for i in num:
    n_bucket[i] += 1
for j, k in n_bucket.items():
    print(k)

# 3052
cnt, arr = 0, []
while cnt < 10:
    num = int(sys.stdin.readline())
    arr.append(num%42)
    cnt += 1
print(len(set(arr)))

# 1546
n = int(input())
arr = list(map(int, input().split()))
new = list(map(lambda x: x/max(arr)*100, arr))
print(sum(new)/n)

# 8958
n = int(input())
for i in range(n):
    l = sys.stdin.readline()
    pts, score = 0, 0
    for j in l:
        if j=='O':
            pts += 1
            score += pts
        else:
            pts = 0
    print(score)

# 4344
n = int(sys.stdin.readline())
for i in range(n):
    arr = list(map(int, (sys.stdin.readline()).split()))
    _m = sum(arr[1:])/arr[0]
    new = list(filter(lambda x: x > _m, arr[1:]))
    val = str(len(new)/arr[0]*100)
    val = val[:6] if len(val) >= 6 else val + "0"*(6-len(val))
    print(f"{val}%")
