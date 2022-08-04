import re
import numpy as np
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i, num in enumerate(nums):
            if target - num in comps:
                return [comps[target - num], i]
            comps[num] = i
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            
            left, right = i + 1, len(nums) -1
            while left < right:
                arr = [nums[i], nums[left], nums[right]]
                sums = sum(arr)
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    results.append(arr)

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -=1
        return results
    
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        storage = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                storage += left_max - height[left]
                left += 1
            else:
                storage += right_max - height[right]
                right -= 1
        return storage

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out, p = [], 1
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums) - 1, - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
    
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board)!=9:
            return False
        board_r = np.array(board)
        board_c = board_r.T
        board_b = board_r.reshape(3, 3, 3, 3).swapaxes(1, 2).reshape(9, -1) # 3*3 박스를 2D 배열화
        for _rows, _cols, _boxs in zip(board_r, board_c, board_b):
            if (len(_rows)!=9)|(len(_cols)!=9)|(len(_boxs)!=9):
                return False

            # rows
            unique, count = np.unique(_rows, return_counts=True)
            for _unq, _cnt in zip(unique, count):
                if (_unq!=".")&(_cnt > 1):
                    return False
            
            # colums
            unique, count = np.unique(_cols, return_counts=True)
            for _unq, _cnt in zip(unique, count):
                if (_unq!=".")&(_cnt > 1):
                    return False
            
            # boxes
            unique, count = np.unique(_boxs, return_counts=True)
            for _unq, _cnt in zip(unique, count):
                if (_unq!=".")&(_cnt > 1):
                    return False
        return True