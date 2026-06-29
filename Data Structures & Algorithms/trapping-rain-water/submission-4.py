class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        i=0
        j=len(height)-1
        l_max=height[i]
        r_max=height[j]
        while i<j:
            if l_max<r_max:
                i+=1
                l_max=max(l_max,height[i])
                result+=l_max-height[i]
            else:
                j-=1
                r_max=max(r_max,height[j])
                result+=r_max-height[j]
        return result