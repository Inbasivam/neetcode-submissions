class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s={}
        for ind,i in enumerate(nums):
            if i in s:
                return True
            else:
                s[i]=ind
        return False
        