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
N = int(input())

def fibo(n):
    if (n == 0):
        return 0

    elif (n == 1):
        return 1

    return fibo(n - 2) + fibo(n - 1)

print(fibo(N))


# 17478
def end_sentence(n):
    if n < 0:
        return
    print("____" * n + '라고 답변하였지.')
    return end_sentence(n-1)

def recursion(n, m):
    print("____" * m + '"재귀함수가 뭔가요?"')
    if n == 0:
        print("____" * m + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        return end_sentence(m)
    print("____" * m + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print("____" * m + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print("____" * m + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    return recursion(n - 1, m + 1)

n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursion(n, 0)


# 2447


# 11729


"""
# 10872, 재귀 함수는 프로그래밍에 있어 중요한 기법 중 하나, 자기 자신을 다시 호출하는 함수라고 하는데 팩토리얼과 같은 기본 연산에서의 재귀적 함수 사용은 알겠는데, 금일 비즈니스 로직에서의 적용 시도는 실패함.
# 10870, 문제를 다르게 이해해서, 계속 오류가 났었던 문제. n번째 피보나치 수를 구하는 것인데, sum of fibos로 착각함.
# 17478, 재귀함수를 참조한 재귀함수, 풀라고 해서 풀었으나 현재 프로젝트에서 이걸 사용해도 될 법한 로직이 생각나지 않음.
"""
