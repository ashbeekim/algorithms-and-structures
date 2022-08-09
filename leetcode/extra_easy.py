from typing import List


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


class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:][::-1]    # bin(n) := '0b' + ~
        n = n + "0"*(32 - len(n))
        return int(n, 2)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        for _ in range(cnt):
            nums.remove(0)
            nums.append(0)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
