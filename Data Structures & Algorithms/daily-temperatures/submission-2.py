class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i,val in enumerate(temperatures):
            while stack and val>stack[-1][1]:
                ind,t=stack.pop()
                result[ind]=i-ind
            stack.append([i,val])
        return result