# 더 맵게
def mixScoville(arr):
    if arr[0] > arr[1]:
        arr = sorted(arr)
    
    a, b = arr[0], arr[1]
    arr = arr[2:]
    arr.insert(0, a+(b*2))
    return arr
    
def solution(scoville, K):
    cnt = 0
    scoville = sorted(scoville)
    
    for i in range(1, len(scoville)):
        if False not in list(map(lambda x: x >= K, scoville)):
            break
            
        scoville = mixScoville(scoville)
        cnt += 1
        
    if len(list(filter(lambda x: x >= K, scoville))) < 1:
            return -1
    
    return cnt

# 디스크 컨트롤러

# 이중우선순위큐

'''
"더 뱁게",,,정확성은 다 통과하는데, 효율성에서 떨어진다고...heapq를 사용해야하는지 우선 더 파악해보고, 일단은 다음 문제로 넘어가겠음
'''