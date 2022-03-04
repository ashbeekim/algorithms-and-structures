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
from itertools import permutations
from math import sqrt, floor

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

'''

'''