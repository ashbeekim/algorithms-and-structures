# 완주하지 못한 선수
from collections import Counter
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = Counter(participant.copy())
    for _k, _v in Counter(completion).items():
        answer[_k] -= _v
        if answer[_k] == 0:
            del(answer[_k])
    answer = [_k if _v==1 else ((_k + ',')*_v)[:-1] for _k, _v in answer.items()]
    return ','.join(answer)