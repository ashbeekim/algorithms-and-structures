from collections import deque


# 기능개발

# 프린터
def printImp(arr, imp):
    p = arr.popleft()
    if p != imp:
        arr.append(p)
    if imp not in arr:
        imp = max(arr)
    return arr, imp

def solution(priorities, location):
    imp, length = max(priorities), len(priorities)
    res = 0
    documents = deque(range(length))
    arr = deque(priorities.copy())
    while location in documents:
        arr, temp = printImp(arr, imp)
        q = documents.popleft()
        if length == 1:
            res += 1
        if (length != len(arr))&(imp == temp):
            res += 1
            if location != q:
                documents.append(q)
        elif (imp != temp):
            length = len(arr)
            res += 1
            if location != q:
                documents.append(q)
        elif (length == len(arr))&(location == q):
            documents.append(q)

    return res

# 다리를 지나는 트럭

# 주식가격

'''
Stack: LIFO(Last In First Out)
Queue: FIFO(First In First Out)
'''