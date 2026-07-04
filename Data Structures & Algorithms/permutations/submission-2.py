class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        result=[]
        num=self.permute(nums[1:])
        for i in num:
            for j in range(0,len(i)+1):
               c=i.copy()        
               c.insert(j,nums[0])
               result.append(c)
        return result