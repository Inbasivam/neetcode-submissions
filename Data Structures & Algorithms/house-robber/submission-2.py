class Solution:
    def rob(self, nums: List[int]) -> int:
        amount=[0]*len(nums)  
        def max_rob(i):
            if i>=len(nums):
                return 0
            if amount[i]!=0:
                return amount[i]
            amount[i]=max(max_rob(i+1),nums[i]+max_rob(i+2))
            return amount[i]
        return max_rob(0)