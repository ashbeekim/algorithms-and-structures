from itertools import permutations
from math import sqrt, floor


# 모의고사
def solution(answers):
    p_1 = [1, 2, 3, 4, 5]
    p_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    answer = []
    for i in range(len(answers)):
        if answers[i] == p_1[i%len(p_1)]:
            score[0] += 1
        if answers[i] == p_2[i%len(p_2)]:
            score[1] += 1
        if answers[i] == p_3[i%len(p_3)]:
            score[2] += 1
    for i in range(len(score)):
        if max(score)==score[i]:
            answer.append(i+1)
    return answer

# 소수찾기
def solution(numbers):
    numbers = list(sorted(numbers))
    nums, num = [], []
    
    for i in list(range(len(numbers))):
        nums += list(map(''.join, permutations(numbers, r=i+1)))
    nums = set(list(map(int, nums)))

    for n in nums:
        if (n>=2)&(n not in num):
            if (True not in list(map(lambda x: n%x==0, range(2, floor(sqrt(n)) + 1)))):
                num.append(n)
    return len(num)
    
# 카펫
def solution(brown, yellow):
    total = brown + yellow
    for row in range(3, total//2):
        col = total // row

        if (((row * col) == total) & (row >= col) & (((col-2) * (row-2)) == yellow)):                
            answer = [row, col]
            break
            
    return answer


'''
카펫 문제를 풀이할 때 고려한 내용
전체 카펫의 가로 혹은 세로는 무조건 3 이상일 수 밖에 없음(brown|yellow|brown 순의 샌드 형식이기 때문)
가로는 세로와 같거나 세로보다 길다고 했기에 전체 타일의 수에서 절반 이하의 범주에 속할 수 있음
'''