# -*- coding: utf-8 -*-
# if
# # 1
A, B = map(lambda x: int(x), input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')
    
# # 2
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
    
# # 3
year = int(input())
if year%400==0:
  print(1)
elif year%4==0 and year%100!=0:
  print(1)
else: 
  print(0)
  
# # 4
X = int(input())
Y = int(input())
if X > 0:
    print(1) if Y > 0 else print(4)
else:
    print(2) if Y > 0 else print(3)
    
# # 5
H, M = map(int, input().split())
time = H*60 + M
time = (time - 45) if (time - 45 >= 0) else (time - 45 + 24*60)
H, M = time//60, time%60
print(" ".join([str(H), str(M)]))

# # 6
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
