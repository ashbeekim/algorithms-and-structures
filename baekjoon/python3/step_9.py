# -*- coding: utf-8 -*-
# recursion
# 10872
N = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(N))


# 10870


# 17478


# 2447


# 11729


"""
# 10872, 재귀 함수는 프로그래밍에 있어 중요한 기법 중 하나, 자기 자신을 다시 호출하는 함수라고 하는데 팩토리얼과 같은 기본 연산에서의 재귀적 함수 사용은 알겠는데, 금일 비즈니스 로직에서의 적용 시도는 실패함.
"""
