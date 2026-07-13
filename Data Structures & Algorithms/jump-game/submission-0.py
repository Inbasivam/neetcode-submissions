class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)-1
        maxReachable=0
        for i in range(len(nums)):
            if i>maxReachable:
                return False 
            maxReachable=max(maxReachable,i+nums[i])
            if i>=n:
                return True
        return True