class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MAX=1
        MIN=1
        res=nums[0]
        for i in nums:
            tempMax=i*MAX
            MAX=max(i,i*MAX,i*MIN)
            MIN=min(i,tempMax,i*MIN)
            res=max(res,MAX)
        return res