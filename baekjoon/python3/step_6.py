# -*- coding: utf-8 -*-
# string
from ast import pattern
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
word = list(map(lambda x: x.upper(), input()))
unq = Counter(word)
unq = dict(sorted(unq.items(), key=lambda x: -x[1]))
key_list = list(unq.keys())
cnt_list = list(unq.values())
if (len(unq)==1):
    print(key_list[0])
elif (len(unq)>=2)&(cnt_list[0]==cnt_list[1]):
    print('?')
elif (len(unq)>=2)&(cnt_list[0]!=cnt_list[1]):
    print(key_list[0])

# 1152
n = sys.stdin.readline()
# assert len(n) <= 1000000
print(len(n.split()))

# 2908
num = list(map(lambda x: int(x[::-1]), input().split()))
print(max(num))

# 5622
number = input().strip()
times = [1 + idx for idx in range(1, 11)]
patterns = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO' 'PQRS', 'TUV', 'WXYZ', '']
total = 0

for n in number:
    for _idx, _v in enumerate(patterns):
        if n in _v:
            total += times[_idx]
print(total)

# 2941
word = input()
rules = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in rules:
    word = word.replace(i, " ")
print(len(word))

# 1316
def checkGroupWord(letter):
    letters, res = [], 0
    for idx, char in enumerate(letter):
        if char in letters:
            if letter[idx-1]==char:
                pass
            else:
                res+=1
                break
        else:
            letters.append(char)
    return 0 if res else 1

N = int(sys.stdin.readline())
result = 0
for i in range(N):
    letter = sys.stdin.readline().strip()
    result += checkGroupWord(letter)
print(result)

'''
# 1157 IndexError 왜 생기는지 모르겠음...로컬에서는 두 방법 모두 제대로 결과가 나오는데...하...
        KeyError를 겪고, 로컬에서도 발생한 IndexError를 겪고 제대로 푼 것 같아서 else로 처리한 내용 중 IndexError가 발생할 경우의 수를 제외하도록 코드 수정.
# 1152 `문자열의 길이는 1,000,000을 넘지 않는다`고 해서, `assert len(n) <= 1000000`를 추가했는데 AssertionError 발생함..ㅎㅎ..일단 주석 처리하고 다시 제출하니 통과함.
# 5622 다이얼이 10개라서 당장 생각나는 방법인 반복문으로 해결했지만, 영문으로 인지하는데, 1과 0은 반영을 하지 못한다는 점도 그렇고 약간 찝찝함.
'''
