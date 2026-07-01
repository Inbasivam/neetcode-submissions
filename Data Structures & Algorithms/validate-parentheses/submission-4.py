class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={'(':')','[':']','{':'}'}
        for c in s:
            if c in check.keys():
                stack.append(c)
            elif c in check.values():
                if not stack:
                    return False
                else:
                    value=stack.pop()
                    if check[value]!=c:
                        return False
        return not stack