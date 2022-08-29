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
