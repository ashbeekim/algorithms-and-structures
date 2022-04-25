from collections import deque


# 기능개발

# 프린터
def solution(priorities, location):
    res = 0
    documents = deque([(priorities[idx], idx) for idx in range(len(priorities))])
    imp = max(list(map(lambda x: x[0], documents)))
    while location in list(map(lambda x: x[1], documents)):
        temp = max(list(map(lambda x: x[0], documents)))
        doc, idx = documents.popleft()
        if len(documents) == 0:
            res += 1
            break
        if (temp==imp)&(doc==temp):
            res += 1
            if idx != location:
                documents.append((doc, idx))
        else:
            if doc != temp:
                documents.append((doc, idx))
            else:
                res += 1
                if idx != location:
                    documents.append((doc, idx))
    return res

# 다리를 지나는 트럭

# 주식가격
def solution(prices):
    answer = []
    for idx, p in enumerate(prices[:-1]):
        temp = list(map(lambda x: x >= p, prices))
        temp = temp[idx+1:]
        res = 0
        for t in temp:
            if t:
                res += 1
            else:
                res += 1
                break
        answer.append(res)
    answer.append(0)
    return answer
    
'''
Stack: LIFO(Last In First Out)
Queue: FIFO(First In First Out)
'''