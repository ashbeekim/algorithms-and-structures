# -*- coding: utf-8 -*-
# string
from dataclasses import replace
import sys
from collections import Counter

# 11654
x = input()
print(ord(x))

# 11720
x = int(input())
y = list(map(int, list(input())))
assert (x>=1)&(x<=100)&(len(y)==x)
print(sum(y))

# 10809
word = input()
alphabet, new = list('abcdefghijklmnopqrstuvwxyz'), dict()
for _v, _k in enumerate(word):
    if new.get(_k) is None:
        new[_k] = _v
result = list(map(lambda x: str(new.get(x)) if x in new.keys() else "-1", alphabet))
print(" ".join(result))

# 2675
T = int(input())
assert (T>=1)&(T<=1000)
for i in range(T):
    R, S = input().split()
    assert (int(R)>=1)&(int(R)<=8)
    S = list(map(lambda x: x*int(R), list(S)))
    print("".join(S))

# 1157
## trial 1. IndexError
word = input()
assert len(word)<=1000000
word = Counter(list(word.lower()))
word = sorted(word.items(), key=lambda x: -x[1])
if (len(word)>=2)&(word[0][1]==word[1][1]):
    print('?')
else:
    print((word[0][0].upper())
## trial 2. IndexError
word = list(map(lambda x: x.upper(), input()))
assert len(word)<=1000000
unq = dict(map(lambda x: (x, 0), set(word)))
for _k, _v in unq.items():
    _n = list(filter(lambda x: x==_k, word))
    unq[_k] += len(_n)
unq = sorted(unq.items(), key=lambda x: -x[1])
key = list(map(lambda x: x[0], unq))
val = list(map(lambda x: x[1], unq))
if (len(unq)>=2)&(val[0]==val[1]):
    print('?')
else:
    print(key[0])

# 1152
n = sys.stdin.readline()
# assert len(n) <= 1000000
print(len(n.split()))

# 2908
num = list(map(lambda x: int(x[::-1]), input().split()))
print(max(num))

# 5622

# 2941
word = input()
rules = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in rules:
    word = word.replace(i, " ")
print(len(word))

# 1316

'''
# 1157 IndexError 왜 생기는지 모르겠음...로컬에서는 두 방법 모두 제대로 결과가 나오는데...하...
# 1152 `문자열의 길이는 1,000,000을 넘지 않는다`고 해서, `assert len(n) <= 1000000`를 추가했는데 AssertionError 발생함..ㅎㅎ..일단 주석 처리하고 다시 제출하니 통과함.
'''
