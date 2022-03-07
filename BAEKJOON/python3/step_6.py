# -*- coding: utf-8 -*-
# function
# 15596


# 4673
def d(n=10000):
    n_range = list(map(str, range(1, n+1)))
    sum_range = [int(i) + sum(list(map(int, i))) for i in n_range]
    n_range = list(map(int, n_range))
    return sorted(set(n_range) - set(sum_range))
self_num = d()
for i in self_num:
    print(i)

# 1065
n = input()
assert int(n)<=1000
def hansu(n):
    # 한수: 각 자리수가 등차수열을 이룸
    if len(n) < 3:
        return int(n)
    else:
        hansu = 99
        n_range = list(map(str, range(100, int(n)+1)))
        for i in n_range:
            if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
                hansu += 1
        return hansu
print(hansu(n))
