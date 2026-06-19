class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for ind,i in enumerate(nums):
            diff=target-i
            if diff in s:
                return [s[diff],ind]
            s[i]=ind