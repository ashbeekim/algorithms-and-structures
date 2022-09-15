from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        
        for _ in range(n):
            right = right.next
        
        if not right:
            return head.next
            
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return head


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cnt, diff = 0, [0] * len(prices)
        for i in range(1, len(prices)):
            diff[i - cnt] = prices[i] - prices[i - 1]
            if diff[i - cnt] <= 0:
                diff.pop(i - cnt)
                cnt += 1
        return sum(diff)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)
