# -*- coding: utf-8 -*-
# math1
import sys
import math


# 1712
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)


# 2292
N = int(input())
center = 1
last = 0
while True:
    if N > center:
        last += 1
        center = center + last * 6
    else:
        print(last + 1)
        break


# 1193

# 2869
A, B, V = map(int, sys.stdin.readline().split())
day = (V - B) / (A - B)
print(math.ceil(day))


# 10250
for _ in range(int(input())):
    H, W, N = map(int, input().split())
    a = N % H
    b = N // H + 1
    if a == 0:
        a = H
        b -= 1
    print(a * 100 + b)


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


"""
# 2292
    # 처음에 if, else의 순서를 다르게 이해하고 작성해서, 시간초과에 빠짐. 예상 못한 규칙이라면 반영이 되지 않도록 해야 함.
# 2869
    # 수식을 어떻게 작성하냐에 따라 코드도 줄일 수 있고, 시간도 줄일 수 있다는 점은 프젝에도 적용시키고 싶을 정도!
# 10250
    # 연산의 순서가 분명하다면, 굳이 괄호로 묶을 필요는 없음.
"""
