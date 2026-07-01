class Solution:
    def isValid(self, s: str) -> bool:
        check={')':'(','}':'{',']':'['}
        stack=[]
        for c in s:
            if c in check.keys():
                if stack and stack[-1]==check[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False