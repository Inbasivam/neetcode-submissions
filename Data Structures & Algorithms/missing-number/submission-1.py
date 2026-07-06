class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum_=int(n*(n+1)/2)
        actual=0
        for i in range(n):
            actual+=nums[i]
        result=sum_-actual
        return result