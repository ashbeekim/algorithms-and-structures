# -*- coding: utf-8 -*-
# if
'''
마지막 문제는 쉬운 내용을 어렵게 푼 감이 없잖아 들지만...당시의 최선이었음.
'''
# 1330
A, B = map(lambda x: int(x), input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')
    
# 9498
score = int(input())
if score in range(90,101):
    print('A')
elif score in range(80,90):
    print('B')
elif score in range(70,80):
    print('C')
elif score in range(60,70):
    print('D')
else:
    print('F')
    
# 2753
year = int(input())
if year%400==0:
  print(1)
elif year%4==0 and year%100!=0:
  print(1)
else: 
  print(0)
  
# 14681
X = int(input())
Y = int(input())
if X > 0:
    print(1) if Y > 0 else print(4)
else:
    print(2) if Y > 0 else print(3)
    
# 2884
H, M = map(int, input().split())
time = H*60 + M
time = (time - 45) if (time - 45 >= 0) else (time - 45 + 24*60)
H, M = time//60, time%60
print(" ".join([str(H), str(M)]))

# 2525
A, B = map(int, input().split(' '))
C = int(input())
assert A in range(24)
assert B in range(60)
assert C in range(1000)
H, M = C//60, C%60
if B + M <= 59:
    M = B + M
    H = H + A
else:
    M = B + M - 60
    H = H + A + 1
if H > 23:
    H = H - 24
print(H, M, sep=' ')

# 2480
dice = dict([(i+1,0) for i in range(6)])
nums = list(map(lambda x: int(x), input().split()))
for i in nums:
    assert (i>=1)&(i<=6)
    dice[i] += 1
price = 0
sortDice = sorted(dice.items(), key=lambda x: (-x[1], -x[0]))
if sortDice[0][1] == 3:
    print(10000 + sortDice[0][0] * 1000)
elif sortDice[0][1] == 2:
    print(1000 + sortDice[0][0] * 100)
else:
    print(sortDice[0][0] * 100)
