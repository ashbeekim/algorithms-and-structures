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
