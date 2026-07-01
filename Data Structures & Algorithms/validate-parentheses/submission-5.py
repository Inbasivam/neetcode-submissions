class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={'(':')','[':']','{':'}'}
        for c in s:
            if c in check.keys():
                stack.append(c)
            elif stack and check[stack[-1]]==c:
                value=stack.pop()
            else:
                return False
        return not stack