import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, bucket, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -= 1
            if char in bucket:
                continue
            while stack and char<stack[-1] and counter[stack[-1]]>0:
                bucket.remove(stack.pop())
            stack.append(char)
            bucket.add(char)
        return ''.join(stack)
