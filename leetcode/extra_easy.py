class Solution:
    def isPalindrome(self, x: int) -> bool: # 9. Palindrome Number
        if x == 0:
            return True
        elif x > 0:
            num = len(str(x)) // 2
            if len(str(x)) % 2 == 0:
                st, ed = str(x)[:num], str(x)[num:]
                if st == ed[::-1]:
                    return True
            else:
                st, ed = str(x)[:num], str(x)[num + 1:]
                if st == ed[::-1]:
                    return True
        return False


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        for _ in range(max_num + 1):
            if _ not in nums:
                return _
        return max_num + 1
