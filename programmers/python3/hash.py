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

# 전화번호 목록
def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    t_len = len(phone_book)
    assert (t_len>=1)&(t_len<=1000000)
    len_phone = [len(n) for n in phone_book]
    len_phone = list(filter(lambda x: x if (x>=1)&(x<=20) else None, len_phone))
    assert None not in len_phone
    
    len_phone = Counter(len_phone)
    i = 0
    answer = True
    for _len, _cnt in len_phone.items():
        check = list(map(lambda x: x[:_len] in phone_book[i:i+_cnt], phone_book[i+_cnt:]))
        i += _cnt
        if True in check:
            answer = False
            return answer
    return answer

def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    t_len = len(phone_book)
    assert (t_len>=1)&(t_len<=1000000)
    len_phone = [len(n) for n in phone_book]
    len_phone = list(filter(lambda x: x if (x>=1)&(x<=20) else None, len_phone))
    assert None not in len_phone
    
    len_phone = Counter(len_phone).most_common()
    ############################### 수정 중 ###############################
    i = 0
    answer = True
    for _len, _cnt in len_phone.items():
        _comp = phone_book[i:i+_cnt]
        _book = phone_book[i+_cnt:]
        _check = list(map(lambda x: x[:_len] in _comp, _book))
        i += _cnt
        if True in _check:
            answer = False
            return answer
    return answer

# 위장

# 베스트앨범


'''
`완주하지 못한 선수`를 그냥 대충 풀었다가, 정확하지만 효율성이 떨어져서...코드 바꿈
'''