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
N = int(input())

bag = 0

while N >= 0:
    if N % 5 == 0:
        bag = bag + (N // 5)
        print(bag)
        break
    N -= 3
    bag += 1
else:
    print(-1)


# 10757
sum_list = list(map(int, input().split()))
print(sum(sum_list))
