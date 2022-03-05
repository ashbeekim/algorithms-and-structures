# K번째수
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 가장 큰 수
## 1안으로 하면, 1~6?까지 실패라고 출력됨.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: (-int(x[0]), -int(x[-1]))
    return "0" if int("".join(numbers))==0 else "".join(numbers)
## 2안에서도 2를 곱했다가 1~6까지 실패라고 출력되기에 3에서 7까지 다 넣어서 출력해봤는데 모두 통과함.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    return "0" if int("".join(numbers))==0 else "".join(numbers)

# H-Index
def solution(citations):
    answer = 0
    return answer
    
'''
k번째 수를 제출한 뒤, 람다식으로 풀이한 내용을 봤을 땐..ㅋㅋㅋㅋㅋ 함수로 작성하라에 사로잡히지 말자는 다짐을 하게 됨.
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
가장 큰 수를 제출할 때, 2를 초과하는 어떤 수를 넣어도 출력은 되지만 numbers의 원소는 1000 이하라는 점에서 "9"*3="999"가 되니까 큰 수부터 정렬하면 결국 원하는 결과값이 나옴.
제한을 준 내용에서 그 이상의 시도를 할 필요가 없음을 알았지만, 확연하게 연산 속도에 차이가 나기 시작한 시점이 10 정도였던 것으로 기억함.
'''