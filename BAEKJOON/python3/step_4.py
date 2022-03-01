# -*- coding: utf-8 -*-
# while
'''
input으로만 처리하니까 RuntimeError나는 경우가 발생해서 내장 라이브러리 호출함
'''
import sys


# 10952
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        assert (a>0)&(a<10)&(b>0)&(b<10)
        print(a+b)
    except:
        break
    
# 10951
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        assert (a>0)&(a<10)&(b>0)&(b<10)
        print(a+b)
    except:
        break

# 1110
