import os
import sys
import re
from collections import deque, defaultdict, Counter
from typing import List, Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(str) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
    
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[\W]', ' ', paragraph)
            .lower().split()
                 if word not in banned]
        
        counts = Counter(words)
        return counts.most_common(1)[0][0]
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

    def expand(self, s: str, left: int, right: int) -> str:
        # validation & expanding
        # while (left >= 0)&(right < len(s))&(s[left]==s[right]): ## 이렇게 하니까 RuntimeError 발생함
        while (left >= 0) and (right < len(s)) and (s[left]==s[right]):
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        if (len(s) <2)|(s == s[::-1]):
            return s
        result = ''
        for i in range(len(s) - 1):
            result = max(result,\
                        self.expand(s, i, i + 1),\
                        self.expand(s, i, i + 2),\
                        key=len)
        return result
