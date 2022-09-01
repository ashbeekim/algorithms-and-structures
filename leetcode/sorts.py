from heapq import merge
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pts = head
        lst: List = []
        # pointer가 유효할 때까지 배열에 추가
        while pts:
            lst.append(pts.val)
            pts = pts.next
        
        lst = sorted(lst)
        
        pts = head
        # 정렬된 값을 포인터에 재부여
        for _idx in range(len(lst)):
            pts.val = lst[_idx]
            pts = pts.next
        return head


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        section_lst = []
        for _lst in sorted(intervals, key=lambda x: x[0]):
            if section_lst and _lst[0] <= section_lst[-1][1]:
                section_lst[-1][1] = max(section_lst[-1][1], _lst[1])
            else:
                section_lst.append(_lst)
        return section_lst
