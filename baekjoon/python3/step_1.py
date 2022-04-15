# -*- coding: utf-8 -*-
# I/O, +-*/
'''
이전에 풀이했던 때와 최근에 들어갔을 때 문제에서 추가됨
'''
# 2557
print('Hello World!')

# 10718
print('강한친구 대한육군')
print('강한친구 대한육군')

# 10171
print('''\\    /\\
 )  ( ')
(  /  )
 \\(__)|''')

# 10172
print('''|\\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')

# 1000
a, b = map(int, input().split())
print(a+b)

# 1001
a, b = map(int, input().split())
print(a-b)

# 10998
a, b = map(int, input().split())
print(a*b)

# 1008
a, b = map(int, input().split())
print(a/b)

# 10869
a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, end='\n')

# 10430
A, B, C = map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, end='\n')

# ???
a, b = map(int, input().split())
print(a*int(str(b)[-1:]), a*int(str(b)[1:2]), a*int(str(b)[:1]), a*b, end='\n')
# a, b = map(int, str, input().split())
# print(a*int(b[-1:]), a*int(b[1:2]), a*int(b[:1]), a*int(b), end='\n')

######################################################## changed ########################################################

# 10926
id = input().lower()  # 따로 길이에 따른 예외처리는 하지 않음
print(id + "??!")

# 18108
year = int(input())
print(year-543)

# 2588
A = int(input())
B = int(input())
print(A*int(str(B)[-1]))
print(A*int(str(B)[-2]))
print(A*int(str(B)[-3]))
print(A*B)
