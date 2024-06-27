class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if len(stack) == 0:
                    return False
                if mapping[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
    
isValid = Solution().isValid("()")
print(isValid)